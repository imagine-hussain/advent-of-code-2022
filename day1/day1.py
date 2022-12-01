
import contextlib

def main():
    with open("input.txt") as f:
        data = f.read().split("\n\n")
        print(data)
        totals = []
        for d in data:
            nums = d.split("\n")
            with contextlib.suppress(ValueError):
                total = max([int(n) for n in nums])
            # total = sum([int(n) for n in nums])
            totals.append(total)
        # highest_cal_count = max([
        #     sum([
        #         0 if len(num) else int(num)
        #         for num in camel_data.split("\n")
        #     ])
        #     for camel_data in data
        # ])
        # print(highest_cal_count)
        print(totals)
        print(max(totals))


if __name__ == "__main__":
    main()

