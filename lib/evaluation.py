import lib
import numpy as np
import torch


class Evaluation(object):
    def __init__(self, model, loss_func, use_cuda, k=20):
        self.model = model
        self.loss_func = loss_func
        self.topk = k
        self.device = torch.device('cuda' if use_cuda else 'cpu')

    def eval(self, eval_data):
        self.model.eval()
        losses = []
        recalls = []
        mrrs = []
        dataloader = lib.DataLoader(eval_data)
        with torch.no_grad():
            hidden = self.model.init_hidden()
            for input, target, mask in dataloader:
                input = input.to(self.device)
                target = target.to(self.device)
                logit, hidden = self.model(input, hidden)
                logit_sampled = logit[:, target.view(-1)]
                loss = self.loss_func(logit_sampled)
                recall, mrr = lib.evaluate(logit, target, k=self.topk)

                # torch.Tensor.item() to get a Python number from a tensor containing a single value
                losses.append(loss.item())
                recalls.append(recall)
                mrrs.append(mrr)
        mean_losses = np.mean(losses)
        mean_recall = np.mean(recalls)
        mean_mrr = torch.mean(torch.stack(mrrs))

        return mean_losses, mean_recall, mean_mrr