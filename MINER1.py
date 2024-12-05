from hashlib import sha256
import time

MAX_INVOICE = 1000000000

def SHA256(text):
    return sha256(text.encode('utf-8')).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_INVOICE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"YAY| You have mined a bitcoin:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find the correct has after trying {MAX_INVOICE} times")
if __name__ == "__main__":
    transactions = """
        player1 ->player2->200,
        player3->player3->450,
    """
    difficulty = 6

    start = time.time()
    print("Started mining......")
    new_hash = mine(
        5,
        transactions,
        "",
        difficulty,
    )
    total_time = str((time.time() - start))
    print(f"end mining : {total_time} seconds")
    print(new_hash)