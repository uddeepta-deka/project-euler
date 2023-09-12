def count_routes(n):
    res = 1
    for i in range(1, n+1):
        res = int(res * (n + i )/i)
    return res

def main():
    n = 20
    print(f"Possible number of routes for {n} x {n} grid = {count_routes(n)}.")

if __name__ == "__main__":
    main()