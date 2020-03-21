def autoFormatCode(input_file,output_file):
	file =open(input_file,'r')
	input_buffer=file.read()
	file.close()
	input_size=len(input_buffer)
	indent_count=0;
	last_written='\0'
	j=0;
	bracket_count=0;
	file = open(output_file,'w')
	for i in range(input_size-1):
		j=0

		if input_buffer[i] == '(':
			bracket_count+=1
		if input_buffer[i] == ')':
			bracket_count-=1

		if input_buffer[i] == ' ' and last_written == '\n':
			i+=1;
			continue

		if input_buffer[i] == '}':
			indent_count-=1
			if last_written!='\n':
				file.write('\n')
				last_written='\n'

		if last_written=='\n':
			if indent_count != 0:
				while j<indent_count :
					if input_buffer[i+j]=='\t':
						file.write('\t')
						last_written='\t'
						j+=1
						break
					else:
						file.write('\t')
						j+=1

		if input_buffer[i] == '{':
			indent_count+=1
			if input_buffer[i-1] == ')':
				file.write('\n')
				last_written='\n'
				t=indent_count
				while t-1!=0:
					file.write('\t')
					t-=1

		if input_buffer[i] == '\n':
			if input_buffer[i+1] == '\n':
				continue

		if input_buffer[i] == '\t':
			i+=1
			continue

		if input_buffer[i] == ' ' and last_written==' ':
			i+=1
			continue

		if input_buffer[i] == '+' and input_buffer[i+1] !='+' and input_buffer[i-1]!='+':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '-' and input_buffer[i+1] !='-' and input_buffer[i-1]!='-':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '=' and input_buffer[i-1]!='=' and input_buffer[i-1]!='+' and input_buffer[i-1]!='-' and input_buffer[i-1]!='*' and input_buffer[i-1]!='/' and input_buffer[i-1]!='!'  and input_buffer[i-1]!='<'  and input_buffer[i-1]!='>'  and input_buffer[i-1]!='^'  and input_buffer[i-1]!='%' and input_buffer[i-1]!='&' and input_buffer[i-1]!='|'  and (input_buffer[i-1]!='<' and input_buffer[i-2]!='<') and (input_buffer[i-1]!='>' and input_buffer[i-2]!='>'):						
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '*':
			if input_buffer[i-1] !=' 'and input_buffer[i-1] !='/':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '/':
			if input_buffer[i-1] !=' ' and input_buffer[i-1]!='/' and input_buffer == '*':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '%':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '^':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '!':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '&':
			if input_buffer[i-1] !=' ' and input_buffer[i-1] != '&':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '|':
			if input_buffer[i-1] !=' ' and input_buffer[i-1] != '|':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '>' and indent_count!=0:
			if input_buffer[i-1] !=' ' and input_buffer[i-1] != '>':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == '<' and indent_count != 0:
			if input_buffer[i-1] !=' ' and input_buffer[i-1] != '<':
				file.write(' ')
				last_written=' '

		if input_buffer[i] == ';':
			if input_buffer[i-1] !=' ':
				file.write(' ')
				last_written=' '

		file.write(input_buffer[i])
		last_written = input_buffer[i]
		i+=1

		if last_written == '+':
			if input_buffer[i] !='+' and input_buffer[i] != '=' and input_buffer[i-2] != '+':
				file.write(' ')
				last_written = ' '

		if last_written == '-':
			if input_buffer[i] !='-' and input_buffer[i] != '=' and input_buffer[i-2] != '-':
				file.write(' ')
				last_written = ' '

		if last_written == '=':
			if input_buffer[i] !='=':
				file.write(' ')
				last_written = ' '

		if last_written == '/':
			if input_buffer[i] !=' ' and input_buffer[i] != '='and input_buffer[i]!='/' and input_buffer[i]!='*':
				file.write(' ')
				last_written = ' '

		if last_written == '%':
			if input_buffer[i] !=' ' and input_buffer[i] != '=':
				file.write(' ')
				last_written = ' '

		if last_written == '>' and indent_count!=0:
			if input_buffer[i] !=' ' and input_buffer[i] != '=' and input_buffer[i] != '>':
				file.write(' ')
				last_written = ' '

		if last_written == '<' and indent_count!=0:
			if input_buffer[i] !=' ' and input_buffer[i] != '=' and input_buffer[i] != '<':
				file.write(' ')
				last_written = ' '

		if last_written == '|':
			if input_buffer[i] !=' ' and input_buffer[i] != '=' and input_buffer[i] != '|':
				file.write(' ')
				last_written = ' '

		if last_written == '&' and input_buffer[i-2]=='&':
			file.write(' ')
			last_written = ' '

		if last_written == ';' and bracket_count == 0 :
			if input_buffer[i] != '\n' and input_buffer[i] != ' ' and input_buffer[i] != '\t':
				file.write('\n')
				last_written='\n'
	file.close()
