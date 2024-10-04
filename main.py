def process_input(input_str):
    try:
        arr = list(set(int(num) for num in input_str.split() if int(num) > 0))
        
        if not arr:
            print("INVALID INPUTS")
            return

        ascending = sorted(arr)
        descending = sorted(arr, reverse=True)

        print(" ".join(map(str, descending)))
        print(" ".join(map(str, ascending)))
    except ValueError:
        print("INVALID INPUTS")

input_str = input().strip()

process_input(input_str)
