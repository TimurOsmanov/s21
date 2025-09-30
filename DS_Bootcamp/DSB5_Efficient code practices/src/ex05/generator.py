#!/usr/bin/env python3
import sys


def argv_check(my_argv: list) -> tuple:
    if len(my_argv) != 2:
        # if there are no arguments or too many arguments, the program displays nothing
        return ()

    _, path = my_argv
    return _, path


def read_csv(path: str) -> list:
    with open(path, "r") as file:
        for line in file:
            yield line.strip()


def main() -> None:
    try:
        _, path = argv_check(sys.argv)
        my_file: list = read_csv(path)
        for _ in my_file:
            pass

        with open('/proc/self/status', "r") as f_status:
            # https://man7.org/linux/man-pages/man5/proc_pid_status.5.html
            # proc_pid_status(5) — Linux manual page
            # VmPeak Peak virtual memory size (kB), VmRSS and RssAnon are inaccurate

            memusage: str = f_status.read().split('VmPeak:')[1].split('\n')[0][:-3].strip()
            print(f"Peak Memory Usage = {int(memusage)/1024**2:.3f} GB")

        with open('/proc/self/stat', "r") as f_stat:
            # https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html
            # proc_pid_stat(5) — Linux manual page
            # in stats num (starts with 1) 14 - utime, 15 - stime; both measured in clock ticks
            # 22 - The time the process started after system boot expressed in clock ticks

            stats: list = f_stat.read().split()
            with open('/proc/uptime', 'r') as f_uptime:
                # https://man7.org/linux/man-pages/man5/proc_uptime.5.html
                # This file contains two numbers (values in seconds): the uptime of the system
                # (including time spent in suspend) and the amount of time spent in the idle process.

                CLK_TCK: int = round(int(stats[21]) / float(f_uptime.read().split()[0]))
                total_time: float = round(int(stats[13])/CLK_TCK + int(stats[14])/CLK_TCK, 2)
                print(f"User Mode Time + System Mode Time = {total_time}s")

    except Exception as e:
        # also can print Killed - not enough ram
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
