# oui2hash

<h1 align="center"> With oui2hash, you can easily transform the IEEE oui.txt file into a python format hash table. </br> This makes it easy to include in your project as an importable module.</h1>
</br>The hash table is sorted, with keys as the OUI, and the values being the manufacturer string</br></br>

# **Some of the key features are:**

- intake of text oui file from the IEEE website
- parsing the file for the OUI and manufacturer string
- creates a properly formatted python file with the hash table, ready to query

# Requirements:
  - there are no requirements outside of the standard python library.
  - an oui.txt file

# Install:

To install, clone this repo via the following command line code:

```
$git clone git@github.com:theweefies/oui2hash.git
```

Github now requires the use of ssh keys. For information on how to set up ssh keys, [click here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

# **How to run:**
  
  ```
  $./oui2hash.py oui.txt
  ```
  
  Note: you should not need to run sudo with this script, but it was made in windows, so you may need to run it through dos2unix to get it to work.