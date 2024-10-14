# FastText: A Comprehensive Guide

## Table of Contents
- [1. What is fastText?](#1-what-is-fasttext)
- [2. n-gram Word Representation](#2-n-gram-word-representation)
- [3. fastText Model Architecture](#3-fasttext-model-architecture)
- [4. Core Concepts of fastText](#4-core-concepts-of-fasttext)
- [5. Classification Performance](#5-classification-performance)
- [6. Differences between fastText and Word2Vec](#6-differences-between-fasttext-and-word2vec)
- [7. Code Implementation](#7-code-implementation)
- [8. References](#8-references)

## 1. What is fastText?

fastText introduces subword embeddings, which capture the internal structure and morphological relationships of words. For example, the words "dog," "dogs," and "dogcatcher" all share the root "dog" but have different suffixes. Unlike Word2Vec, where different words have distinct vectors, fastText uses subword information to build relationships between similar words.

In fastText, text classification also generates word embeddings, unless you are training the model with pre-trained embeddings.

## 2. n-gram Word Representation

In Word2Vec, each word is treated as an atomic unit, missing out on morphological similarities between words. To overcome this, fastText represents words using character-level n-grams. For example, for the word "book" with n=3, the trigrams would be:

- `<bo`, `boo`, `ook`, `ok>`

These trigrams are then used to represent the word's vector. This approach:

1. Improves vector generation for low-frequency words.
2. Enables vector construction for out-of-vocabulary words by combining their character-level n-grams.

## 3. fastText Model Architecture

fastText’s architecture is similar to Word2Vec’s Continuous Bag of Words (CBOW) model but includes key differences. The architecture comprises three layers: input, hidden, and output (hierarchical softmax).

- **Input:** Context words represented by their n-gram features.
- **Hidden Layer:** Embeddings are averaged over all input vectors.
- **Output Layer:** Outputs the target class for text classification.

Key distinctions:
- fastText inputs include word embeddings and n-grams, whereas CBOW uses one-hot encoded words.
- fastText outputs document labels, while CBOW outputs target words.

## 4. Core Concepts of fastText

The essence of fastText lies in two techniques:
1. **n-gram Features:** Character-level n-grams help represent words, improving classification performance.
2. **Hierarchical Softmax:** Reduces training time while maintaining classification accuracy.

fastText averages word and n-gram vectors to generate document representations, which are then used in a softmax classifier for multi-class classification.

## 5. Classification Performance

fastText often rivals traditional non-linear classifiers. Consider two sentences:

- "肚子 饿了 我 要 吃饭"  
- "肚子 饿了 我 要 吃东西"

These sentences have nearly identical meanings and should belong to the same class. Traditional classifiers might generate very different vectors for these sentences due to differences in TF-IDF values. However, fastText, using word embeddings, produces similar document vectors for semantically similar sentences.

## 6. Differences between fastText and Word2Vec

While both fastText and Word2Vec share similar architectures and optimization methods, such as hierarchical softmax, they have distinct purposes:

|      | Word2Vec                             | fastText                              |
| ---- | ------------------------------------ | ------------------------------------- |
| Input | One-hot encoded word vectors        | Embedded word and n-gram vectors      |
| Output| Predicts a target word              | Predicts a class label                |

fastText uses hierarchical softmax for classification, fully utilizing its capabilities to efficiently handle large datasets and multilingual tasks.

### Advantages of fastText:
1. **Efficient on Large Data:** Trains quickly, processing over a billion words in under 10 minutes on standard CPUs.
2. **Multilingual Support:** Works well across multiple languages including English, German, Spanish, and French.
3. **Specializes in Text Classification:** Achieves state-of-the-art performance on tasks like sentiment analysis and label prediction.

## 7. Code Implementation

You can download the Tsinghua Text Classification dataset [here](https://thunlp.oss-cn-qingdao.aliyuncs.com/THUCNews.zip).

Check out the [fastText implementation for news classification](https://github.com/NLP-LOVE/ML-NLP/blob/master/NLP/16.2%20fastText/fastText.ipynb).

## 8. References

- [fastText Overview and Application](http://www.52nlp.cn/fasttext)

---

> Author: [@mantchs](https://github.com/NLP-LOVE/ML-NLP)  
> GitHub: [https://github.com/NLP-LOVE/ML-NLP](https://github.com/NLP-LOVE/ML-NLP)  
> Join the discussion and improve this project together! Group ID: 【541954936】  
> <img border="0" src="http://pub.idqqimg.com/wpa/images/group.png" alt="NLP面试学习群" title="NLP面试学习群">