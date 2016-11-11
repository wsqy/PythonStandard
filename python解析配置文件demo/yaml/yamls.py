import yaml
f = open('test.yaml')
# xx = {"name": "qy", "age": 21, "happy": [1, 2, 3, 4]}
# yaml.dump(xx, f)
x = yaml.load(f)
print(x)
