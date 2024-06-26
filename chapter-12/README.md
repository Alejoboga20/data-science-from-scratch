# Chapter 12: K-Nearest Neighbors

The model is based on the assumption that similar things exist in close proximity. The requirements for this model are:

- Some notion of distance.
- Things that are near each other are similar.

An example of this model is the k-nearest neighbors algorithm. This algorithm is based on the idea that similar things exist in close proximity. The algorithm works as follows. We just take the most common label and break the tie if necessary.

```python
def majority_vote(labels: List[str]) -> str:
    """Assumes that labels are ordered from nearest to farthest."""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest

# Tie, so look at first 4, then 'b'
assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'
```

We have to be careful when selecting k. If k is too small, the model will be too sensitive to noise in the training data. If k is too large, the model will fail to capture the complexity of the data. Usually, we use cross-validation to select the best k.
