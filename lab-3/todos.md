# TODOs

## Design

- Define Pipeline
- [x] Define Packages

## Coding

- Define IO
- [x] Define Overall Program Flow
- [x] Add docstrings to normalize package
- [x] Remove prioritize package
- [ ] Priority queue
  - [ ] Percolate
  - [ ] Enqueue
  - [ ] Dequeue
- [ ] Huffman Encoding Tree
  - [ ] Adapt implementation from ZyBook
  - [ ] Adpat compress implementation


```java
HuffmanBuildTree(inputString) {
   // First build the frequency table
   table = BuildCharacterFrequencyTable(inputString)

   // Make a priority queue of nodes
   nodes = new PriorityQueue()
   for ((character, frequency) in table) {
      newLeaf = new LeafNode(frequency, character)
      Enqueue newLeaf into nodes
   }
   // Make parent nodes up to the root
   while (nodes⇢length > 1) {
      // Dequeue 2 lowest-priority nodes
      left = Dequeue from nodes
      right = Dequeue from nodes

      // Make a parent for the two nodes
      freqSum = right⇢frequency + left⇢frequency
      parent = new InternalNode(freqSum, left, right)

      // Enqueue parent back into priority queue
      Enqueue parent into nodes
   }
   return Dequeue from nodes
}

treeRoot = HuffmanBuildTree("BANANAS")
```

```java
HuffmanGetCodes(node, prefix, output) {
   if (node is a leaf)
      output[node⇢character] = prefix
   else {
      HuffmanGetCodes(node⇢left, prefix + "0", output)
      HuffmanGetCodes(node⇢right, prefix + "1", output)
   }
   return output
}

root = HuffmanBuildTree("BANANAS")
codes = HuffmanGetCodes(root, "", new Dictionary())
```

```java
HuffmanCompress(inputString) {
   // Build the Huffman tree
   root = HuffmanBuildTree(inputString)

   // Get the compression codes from the tree
   codes = HuffmanGetCodes(root, "", new Dictionary())
   
   // Build the compressed result
   result = ""
   for c in inputString {
      result += codes[c]
   }
   return result and root
}

HuffmanDecompress(compressedString, treeRoot) {
   node = treeRoot
   result = ""
   for (bit in compressedString) {
      // Go to left or right child based on bit value
      if (bit == 0)
         node = node⇢left
      else
         node = node⇢right

      // If the node is a leaf, add the character to the 
      // decompressed result and go back to the root node
      if (node is a leaf) {
         result += node⇢character
         node = treeRoot
      }
   }
   return result
}
```



## Docs

- Write README

## Analysis

### Enhancements

- [ ] Custom generator tree iteration by adding parameter to built in __iter__ function, with default of preorder
