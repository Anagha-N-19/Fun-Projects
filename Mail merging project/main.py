infile1 = open('starting_letter.txt', 'r')
s1 = infile1.read()
infile2 = open('invited_names.txt', 'r')
s2 = infile2.read()
s2 = s2.split('\n')
for name in s2:
    outfile = open(f'./output letters/letter_to_{name}.txt', 'w')
    output_letter = s1.replace('[name]', name)
    outfile.write(output_letter)
