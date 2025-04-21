import os
import random

def split_files(folder_path, train_ratio=0.8, seed=42):
    """
    Splits files in a folder into training and validation sets.

    Args:
        folder_path (str): Path to the folder containing files.
        train_ratio (float): Ratio of files to include in the training set.
        seed (int): Random seed for reproducibility.

    Returns:
        tuple: Two lists containing training and validation file paths.
    """
    random.seed(seed)
    files = [os.path.abspath(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]    
    random.shuffle(files)
    split_index = int(len(files) * train_ratio)
    train_files = files[:split_index]
    val_files = files[split_index:]

    return train_files, val_files

if __name__ == "__main__":
    folder_path = "/home/tang/PPG-Mel/fac-via-ppg/recordings/koren_YKWK"  # Replace with your folder path
    train_files, val_files = split_files(folder_path)

    # Save the results to text files
    with open("training-set-koren-YKWK.txt", "w") as train_file:
        train_file.write("\n".join(train_files))

    with open("validation-set-koren-YKWK.txt", "w") as val_file:
        val_file.write("\n".join(val_files))

    print(f"Training set: {len(train_files)} files")
    print(f"Validation set: {len(val_files)} files")