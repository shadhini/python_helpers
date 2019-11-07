import sys

try:
    try:
        print(45/0)
    except Exception:
        print("exit:: Exception occured")
        exit(1)
    finally:
        print("exit:: End of process")
    print("exit:: a b c")
except Exception:
    print("exit:: Exception in outer tyr catch")
finally:
    print("exit:: End of outer process")

# try:
#     try:
#         print(45/0)
#     except Exception:
#         print("sys.exit:: Exception occured")
#         sys.exit(1)
#     finally:
#         print("sys.exit:: End of process")
#     print("sys.exit:: a b c")
# except Exception:
#     print("sys.exit:: Exception in outer tyr catch")
# finally:
#     print("sys.exit:: End of outer process")
