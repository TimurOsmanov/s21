import analytics
import config


def main() -> None:
    obj: analytics.Research() = analytics.Research()
    data: list = obj.file_reader()

    try:
        obs_len: int = len(data)

        obj1: analytics.Research.Calculations = analytics.Research().Calculations(data)
        count: tuple = obj1.count()
        tails, heads = count

        fractions: tuple = obj1.fractions(count)
        prob1, prob2 = fractions

        obj2: analytics.Research.Analytics = analytics.Research.Analytics(data)
        observations: list = obj2.predict_random(config.num_of_steps)

        obj3: analytics.Research.Analytics = analytics.Research.Analytics(observations)
        p_tails, p_heads = obj3.count()

        report = config.report.format(obs=obs_len, tails=tails, tails_end='s' if tails > 1 else '',
                                   heads=heads, heads_end='s' if heads > 1 else '',
                                   prob1=prob1, prob2=prob2,
                                   p_tails=p_tails, p_tails_end='s' if p_tails > 1 else '',
                                   p_heads=p_heads, p_heads_end='s' if p_heads > 1 else '')

        obj.tg_msg("The report has been successfully created")
        obj2.save_file("report","txt", report)

    except TypeError:
        obj.tg_msg(f"The report hasn’t been created due to an error: {data}")
        print(f"Error: {data}")


if __name__ == "__main__":
    main()
