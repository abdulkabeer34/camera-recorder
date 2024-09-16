# Video Record Project

Use to recrd videos and images in python 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install opencv-python
```

## Usage

run this program by giving parameters and there name before the parameter with "--" 

```bash
  ## examples   
  python main.py --video --delay 3 duration 5 --path video.avi
  python main.py --image --delay 3 amount 5 --path image.jpeg
  python main.py --image 
  python main.py --video
```

# Required Parameters
```python
 --video  
 --image
```

# Optional Paramters 
```python
 ["--duration","--delay","--path"]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)