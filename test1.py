'''
Input:
{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

Output:
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
'''


class FileOwner:
    @staticmethod
    def group_by_owner(data):
        n = list(set(data.values()))
        new_dict = dict((value, []) for value in n)
        for key, value in data.items():
            if value in new_dict:
                new_dict[value].append(key)
        return new_dict


data = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwner.group_by_owner(data))
