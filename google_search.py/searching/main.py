from googlesearch import search;

query = input("Type the terms to search: ");
num_results = int(input('Entry the minimal results: '));

result = list(search(query, lang = 'pt-br', num_results = num_results));

print(result);
