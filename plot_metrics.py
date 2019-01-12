from matplotlib import pyplot as plt



models = [("baseline", "rc_models_20"), ("Model 1", "rc_models_modified_20"), ("Model 2", "rc_models_modified_full_20"), ("Model 3", "rc_models_modified_full_noA_20")]

train_f1 = "train_f1_epoch.txt"
dev_f1 = "dev_f1_epoch.txt"
train_em = "train_em_epoch.txt"
dev_em = "dev_em_epoch.txt"
train_loss = "train_loss_epoch.txt"

def plot_metrics():

    for (model_name, model_dir) in models:
        train_f1_vals = []
        dev_f1_vals = []
        train_em_vals = []
        dev_em_vals = []
        train_loss_vals = []
        with open(model_dir + "/metrics/" + train_f1, "r") as file:
            for line in file:
                train_f1_vals.append(float(line))

        with open(model_dir + "/metrics/" + dev_f1, "r") as file:
            for line in file:
                dev_f1_vals.append(float(line))

        with open(model_dir + "/metrics/" + train_em, "r") as file:
            for line in file:
                train_em_vals.append(float(line))

        with open(model_dir + "/metrics/" + dev_em, "r") as file:
            for line in file:
                dev_em_vals.append(float(line))

        with open(model_dir + "/metrics/" + train_loss, "r") as file:
            for line in file:
                train_loss_vals.append(float(line))

        plt.plot([i for i in range(1, len(train_f1_vals) + 1)],train_f1_vals, label="Train F1 score")
        plt.plot([i for i in range(1, len(dev_f1_vals) + 1)], dev_f1_vals, label="Dev F1 score")
        plt.plot([i for i in range(1, len(train_em_vals) + 1)], train_em_vals, label="Train EM score")
        plt.plot([i for i in range(1, len(dev_em_vals) + 1)], dev_em_vals, label="Dev EM score")
        plt.xlabel("Epochs")
        plt.ylabel("Metric value")
        plt.legend()
        plt.show()

        plt.plot([i for i in range(1, len(train_loss_vals) + 1)], train_loss_vals)
        plt.xlabel("Epochs")
        plt.ylabel("Train loss")
        plt.show()

if __name__ == '__main__':
    plot_metrics()