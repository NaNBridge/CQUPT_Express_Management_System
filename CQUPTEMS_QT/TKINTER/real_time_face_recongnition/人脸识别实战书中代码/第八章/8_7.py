import pickle
import  numpy as np
import os
def get_cifar100_train_data_and_label(root = ""):
    def load_file(filename):
        with open(filename, 'rb') as fo:
            data = pickle.load(fo, encoding='latin1')
        return data
    data_batch_1 = load_file(os.path.join(root, 'data_batch_1'))
    data_batch_2 = load_file(os.path.join(root, 'data_batch_2'))
    data_batch_3 = load_file(os.path.join(root, 'data_batch_3'))
    data_batch_4 = load_file(os.path.join(root, 'data_batch_4'))
    data_batch_5 = load_file(os.path.join(root, 'data_batch_5'))
    dataset = []
    labelset = []
    for data in [data_batch_1,data_batch_2,data_batch_3,data_batch_4,data_batch_5]:
        img_data = (data["data"])
        img_label = (data["labels"])
        dataset.append(img_data)
        labelset.append(img_label)
    dataset = np.concatenate(dataset)
    labelset = np.concatenate(labelset)
    return dataset,labelset
def get_cifar100_test_data_and_label(root = ""):
    def load_file(filename):
        with open(filename, 'rb') as fo:
            data = pickle.load(fo, encoding='latin1')
        return data
    data_batch_1 = load_file(os.path.join(root, 'test_batch'))
    dataset = []
    labelset = []
    for data in [data_batch_1]:
        img_data = (data["data"])
        img_label = (data["labels"])
        dataset.append(img_data)
        labelset.append(img_label)
    dataset = np.concatenate(dataset)
    labelset = np.concatenate(labelset)
    return dataset,labelset

def get_CIFAR100_dataset(root = ""):
    train_dataset,label_dataset = get_cifar100_train_data_and_label(root=root)
    test_dataset,test_label_dataset = get_cifar100_train_data_and_label(root=root)
    return  train_dataset,label_dataset,test_dataset,test_label_dataset
if __name__ == "__main__":
    get_CIFAR100_dataset(root="../cifar-10-batches-py/")
