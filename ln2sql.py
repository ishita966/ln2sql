#!/usr/bin/env python
# coding: utf-8

# In[122]:


import sys, re
import unicodedata
import imp
imp.reload(sys)
#sys.setdefaultencoding("utf-8")

class LangConfig:

	def __init__(self):
		self.avg_keywords = []
		self.sum_keywords = []
		self.max_keywords = []
		self.min_keywords = []
		self.count_keywords = []
		self.junction_keywords = []
		self.disjunction_keywords = []
		self.greater_keywords = []
		self.less_keywords = []
		self.between_keywords = []
		self.order_by_keywords = []
		self.group_by_keywords = []
		self.negation_keywords = []

	def get_avg_keywords(self):
		return self.avg_keywords

	def get_sum_keywords(self):
		return self.sum_keywords

	def get_max_keywords(self):
		return self.max_keywords

	def get_min_keywords(self):
		return self.min_keywords

	def get_count_keywords(self):
		return self.count_keywords

	def get_junction_keywords(self):
		return self.junction_keywords

	def get_disjunction_keywords(self):
		return self.disjunction_keywords

	def get_greater_keywords(self):
		return self.greater_keywords

	def get_less_keywords(self):
		return self.less_keywords

	def get_between_keywords(self):
		return self.between_keywords

	def get_order_by_keywords(self):
		return self.order_by_keywords

	def get_group_by_keywords(self):
		return self.group_by_keywords

	def get_negation_keywords(self):
		return self.negation_keywords

	def remove_accents(self, string):
		nkfd_form = unicodedata.normalize('NFKD', str(string))
		return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

	def load(self, path):
		with open(path) as f:
			content = f.readlines()
			self.avg_keywords = list(map(self.remove_accents, list(map(str.strip, content[0].replace(':',',').split(",")))))
			self.avg_keywords = self.avg_keywords[1:len(list(self.avg_keywords))]
			self.sum_keywords = list(map(self.remove_accents, list(map(str.strip, content[1].replace(':',',').split(",")))))
			self.sum_keywords = self.sum_keywords[1:len(list(self.sum_keywords))]
			self.max_keywords =list(map(self.remove_accents, list(map(str.strip, content[2].replace(':',',').split(",")))))
			self.max_keywords = self.max_keywords[1:len(list(self.max_keywords))]
			self.min_keywords = list(map(self.remove_accents, list(map(str.strip, content[3].replace(':',',').split(",")))))
			self.min_keywords = self.min_keywords[1:len(list(self.min_keywords))]
			self.count_keywords = list(map(self.remove_accents, list(map(str.strip, content[4].replace(':',',').split(",")))))
			self.count_keywords = self.count_keywords[1:len(list(self.count_keywords))]
			self.junction_keywords = list(map(self.remove_accents,list(map(str.strip, content[5].replace(':',',').split(",")))))
			self.junction_keywords = self.junction_keywords[1:len(list(self.junction_keywords))]
			self.disjunction_keywords = list(map(self.remove_accents, list(map(str.strip, content[6].replace(':',',').split(",")))))
			self.disjunction_keywords = self.disjunction_keywords[1:len(list(self.disjunction_keywords))]
			self.greater_keywords = list(map(self.remove_accents, list(map(str.strip, content[7].replace(':',',').split(",")))))
			self.greater_keywords = self.greater_keywords[1:len(list(self.greater_keywords))]
			self.less_keywords = list(map(self.remove_accents, list(map(str.strip, content[8].replace(':',',').split(",")))))
			self.less_keywords = self.less_keywords[1:len(list(self.less_keywords))]
			self.between_keywords = list(map(self.remove_accents, list(map(str.strip, content[9].replace(':',',').split(",")))))
			self.between_keywords = self.between_keywords[1:len(list(self.between_keywords))]
			self.order_by_keywords = list(map(self.remove_accents,list( map(str.strip, content[10].replace(':',',').split(",")))))
			self.order_by_keywords = self.order_by_keywords[1:len(list(self.order_by_keywords))]
			self.group_by_keywords = list(map(self.remove_accents, list(map(str.strip, content[11].replace(':',',').split(",")))))
			self.group_by_keywords = self.group_by_keywords[1:len(list(self.group_by_keywords))]
			self.negation_keywords = list(map(self.remove_accents, list(map(str.strip, content[12].replace(':',',').split(",")))))
			self.negation_keywords = self.negation_keywords[1:len(list(self.negation_keywords))]

	def print_me(self):
		if settings.DEBUG :
			print (self.avg_keywords)
			print (self.sum_keywords)
			print (self.max_keywords)
			print (self.min_keywords)
			print (self.count_keywords)
			print (self.junction_keywords)
			print (self.disjunction_keywords)
			print (self.greater_keywords)
			print (self.less_keywords)
			print (self.between_keywords)
			print (self.order_by_keywords)
			print (self.group_by_keywords)
			print (self.negation_keywords)


# In[55]:


# -*- coding: utf-8 -*

import sys
import unicodedata

imp.reload(sys)
#sys.setdefaultencoding("utf-8")

class Column:
    name = ''
    type = ''
    is_primary = False
    
    def __init__(self, name=None, type=None, is_primary=None):
        if name is None:
            self.name = ''
        else:
            self.name = name
        if type is None:
            self.type = ''
        else:
            self.type = type
        if is_primary is None:
            self.is_primary = False
        else:
            self.is_primary = is_primary

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

    def is_primary(self):
        return self.is_primary


# In[65]:


# -*- coding: utf-8 -*

import sys
import unicodedata

class settings:
    DEBUG=False

imp.reload(sys)
#sys.setdefaultencoding("utf-8")

#from Column import Column

class Table:
    name = ''
    columns = []
    primary_keys = []
    foreign_keys = []
    
    def __init__(self, name=None, columns=None, primary_keys=None):

        if name is None:
            self.name = ''
        else:
            self.name = name
        
        if columns is None:
            self.columns = []
        else:
            self.columns = columns
        
        if primary_keys is None:
            self.primary_keys = []
        else:
            self.primary_keys = primary_keys
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_number_of_columns(self):
        return len(self.columns)
    
    def get_columns(self):
        return self.columns

    def add_column(self, column_name, column_type):
        self.columns.append(Column(column_name, column_type))

    def get_number_of_primary_keys(self):
        return len(self.primary_keys)

    def get_primary_keys(self):
        return self.primary_keys

    def add_primary_key(self, primary_key):
        if settings.DEBUG:
            print ('%s : primary key added:%s' % (self.name, primary_key))
        self.primary_keys.append(primary_key)

    def get_number_of_foreign_keys(self):
        return len(self.foreign_keys)

    def get_foreign_keys(self):
        return self.foreign_keys

    def add_foreign_key(self, col, ref_table, ref_col):
        if settings.DEBUG:
            print ('foreign key added : %s.%s->%s.%s' % (self.name, col, ref_table, ref_col))
        self.foreign_keys.append({'col':col,'ref_table':ref_table,'ref_col':ref_col})



# In[124]:


# -*- coding: utf-8 -*

import sys
import unicodedata

imp.reload(sys)
#sys.setdefaultencoding("utf-8")

class StopwordFilter:
    
    def __init__(self):
        self.list = []
    
    def add_stopword(self, word):
        self.list.append(word)

    def get_stopword_list(self):
        return self.list
    
    def filter(self, sentence):
        tmp_sentence = []
        for word in sentence:
            word = self.remove_accents(word).lower()
            if word not in self.list:
                tmp_sentence.append(word)
        return tmp_sentence

    def remove_accents(self, string):
        nkfd_form = unicodedata.normalize('NFKD', str(string))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def load(self, lang):
        with open('./stopwords/' + lang + '.txt') as f:
            lines = f.read().split('\n')
            for word in lines:
                stopword = self.remove_accents(word).lower()
                self.list.append(stopword)


# In[125]:


# -*- coding: utf-8 -*

import sys
imp.reload(sys)
#sys.setdefaultencoding("utf-8")
import unicodedata

class Thesaurus:
    
    def __init__(self):
        self.dictionnary = {}
    
    def add_entry(self, word, synonyms):
        self.dictionnary[word] = synonyms
    
    def add_synonym_of_a_word(self, word, synonym):
        self.dictionnary[word].append(synonym)
    
    def get_synonyms_of_a_word(self, word):
        if word in self.dictionnary.keys():
            return self.dictionnary[word]

    def remove_accents(self, string):
        nkfd_form = unicodedata.normalize('NFKD', str(string))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def load(self, path):
        with open(path) as f:
            content = f.readlines()
            # we jump content[0] because it is the encoding-type line : useless to parse
            for line_id in range(1,len(content)):
                if '(' not in content[line_id]:
                    line = content[line_id].split("|")
                    word = self.remove_accents(line[0])
                    synonyms = self.remove_accents(content[line_id + 1]).split("|")
                    synonyms.pop(0)
                    self.add_entry(word, synonyms)

    def print_me(self):
        for keys,values in self.dictionnary.items():
            print(keys)
            print(values)


# In[67]:


# -*- coding: utf-8 -*

import sys
import re
import unicodedata

#from Table import Table
#import settings

imp.reload(sys)
#sys.setdefaultencoding("utf-8")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Database:

    def __init__(self):
        self.tables = []

    def get_number_of_tables(self):
        return len(self.tables)

    def get_tables(self):
        return self.tables

    def get_tables_into_dictionnary(self):
        data = {}
        for table in self.tables:
            data[table.name] = []
            for column in table.columns:
                data[table.name].append(column.name)
        return data

    def get_primary_keys_by_table(self):
        data = {}
        for table in self.tables:
            data[table.name] = table.primary_keys
        return data

    def get_primary_keys_of_table(self, table):
        for _table in self.tables:
            if _table.name == table:
                return _table.primary_keys

    def get_foreign_keys_of_table(self, table):
        for _table in self.tables:
            if _table.name == table:
                return _table.get_foreign_keys()

    def add_table(self, table):
        self.tables.append(table)

    def load(self, path):
        with open(path) as f:
            content = f.read()

            tables_string = [p.split(';')[0]
                             for p in content.split('CREATE') if ';' in p]
            for table_string in tables_string:
                if 'TABLE' in table_string:
                    table = self.create_table(table_string)
                    self.add_table(table)

            alter_table_string = [p.split(';')[0]
                                  for p in content.split('ALTER') if ';' in p]
            for s in alter_table_string:
                if 'TABLE' in s:
                    self.alter_table(s)

    def predict_type(self, string):
        if 'int' in string.lower():
            return 'int'
        elif 'char' in string.lower() or 'text' in string.lower():
            return 'string'
        elif 'date' in string.lower():
            return 'date'
        else:
            return 'unknow'

    def create_table(self, table_string):
        lines = table_string.split("\n")
        table = Table()
        for line in lines:
            if 'TABLE' in line:
                table_name = re.search("`(\w+)`", line)
                table.set_name(table_name.group(1))
            elif 'PRIMARY KEY' in line:
                primary_key_columns = re.findall("`(\w+)`", line)
                for primary_key_column in primary_key_columns:
                    table.add_primary_key(primary_key_column)
            else:
                column_name = re.search("`(\w+)`", line)
                if column_name is not None:
                    column_type = self.predict_type(line)
                    table.add_column(column_name.group(1), column_type)
        return table

    def alter_table(self, alter_string):
        lines = alter_string.replace('\n', ' ').split(';')
        for line in lines:
            if 'PRIMARY KEY' in line:
                table_name = re.search("TABLE `(\w+)`", line).group(1)
                table = [t for t in self.tables if t.get_name() == table_name][
                    0]

                primary_key_columns = re.findall(
                    "PRIMARY KEY \(`(\w+)`\)", line)
                for primary_key_column in primary_key_columns:
                    table.add_primary_key(primary_key_column)
            elif 'FOREIGN KEY' in line:
                table_name = re.search("TABLE `(\w+)`", line).group(1)
                table = [t for t in self.tables if t.get_name() == table_name][
                    0]

                foreign_keys_list = re.findall(
                    "FOREIGN KEY \(`(\w+)`\) REFERENCES `(\w+)` \(`(\w+)`\)", line)

                for col, ref_table, ref_col in foreign_keys_list:
                    table.add_foreign_key(col, ref_table, ref_col)

    def print_me(self):
        if settings.DEBUG:
            for table in self.tables:
                print('+-------------------------------------+')
                print("| %25s           |" % (table.name.upper()))
                print('+-------------------------------------+')
                for column in table.columns:
                    if column.name in table.primary_keys:
                        print("| 🔑 %31s           |" % (
                            color.BOLD + column.name + ' (' + column.type + ')' + color.END))
                    else:
                        print("|   %23s           |" %
                              (column.name + ' (' + column.type + ')'))
                print('+-------------------------------------+\n')


# In[69]:


# -*- coding: utf-8 -*

import sys
import unicodedata

#imp.reload(simp.ys)
#sys.setdefaultencoding("utf-8")

class color:
    # PURPLE = '\033[95m'
    # CYAN = '\033[96m'
    # DARKCYAN = '\033[36m'
    # BLUE = '\033[94m'
    # GREEN = '\033[92m'
    # YELLOW = '\033[93m'
    # RED = '\033[91m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'
    # END = '\033[0m'

    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    UNDERLINE = ''
    END = ''

class Select():
	columns = []

	def __init__(self):
		self.columns = []

	def add_column(self, column, column_type):
		if [column, column_type] not in self.columns:
			self.columns.append([column, column_type])

	def get_columns(self):
		return self.columns

	def get_just_column_name(self, column):
		if column != str(None):
			return column.rsplit('.', 1)[1]
		else:
			return column

	def print_column(self, selection):
		column = selection[0]
		column_type = selection[1]

		if column is None:
			if column_type == 'COUNT':
				return color.BOLD + 'COUNT(' + color.END + '*' + color.BOLD + ')' + color.END
			else:
				return '*'
		else:
			if column_type == 'COUNT':
				return color.BOLD + 'COUNT(' + color.END + str(column) + color.BOLD + ')' + color.END
			elif column_type == 'AVG':
				return color.BOLD + 'AVG(' + color.END + str(column) + color.BOLD + ')' + color.END
			elif column_type == 'SUM':
				return color.BOLD + 'SUM(' + color.END + str(column) + color.BOLD + ')' + color.END
			elif column_type == 'MAX':
				return color.BOLD + 'MAX(' + color.END + str(column) + color.BOLD + ')' + color.END
			elif column_type == 'MIN':
				return color.BOLD + 'MIN(' + color.END + str(column) + color.BOLD + ')' + color.END
			else:
				return str(column)

	def __str__(self):
		select_string = ''
		for i in range(0, len(self.columns)):
			if i == (len(self.columns)-1):
				select_string = select_string + str(self.print_column(self.columns[i]))
			else:
				select_string = select_string + str(self.print_column(self.columns[i])) + ', '

		return color.BOLD + 'SELECT ' + color.END + select_string

	def print_json(self, output):
		if len(self.columns) >= 1:
			if len(self.columns) == 1:
				output.write('\t"select": {\n')
				output.write('\t\t"column": "' + self.get_just_column_name(str(self.columns[0][0])) + '",\n')
				output.write('\t\t"type": "' + str(self.columns[0][1]) + '"\n')
				output.write('\t},\n')
			else:
				output.write('\t"select": {\n')
				output.write('\t\t"columns": [\n')
				for i in range(0, len(self.columns)):
					if i == (len(self.columns)-1):
						output.write('\t\t\t{ "column": "' + self.get_just_column_name(str(self.columns[i][0])) + '",\n')
						output.write('\t\t\t  "type": "' + str(self.columns[i][1]) + '"\n')
						output.write('\t\t\t}\n')
					else:
						output.write('\t\t\t{ "column": "' + self.get_just_column_name(str(self.columns[i][0])) + '",\n')
						output.write('\t\t\t  "type": "' + str(self.columns[i][1]) + '"\n')
						output.write('\t\t\t},\n')
				output.write('\t\t]\n')
				output.write('\t},\n')
		else:
			output.write('\t"select": {\n')
			output.write('\t},\n')

class From():
	table = ''

	def __init__(self, table=None):
		if table is not None:
			self.table = table
		else:
			self.table = ''

	def set_table(self, table):
		self.table = table

	def get_table(self):
		return self.table

	def __str__(self):
		return ' ' + color.BOLD + 'FROM ' + color.END + str(self.table)

	def print_json(self, output):
		if self.table != '':
			output.write('\t"from": {\n')
			output.write('\t\t"table": "' + str(self.table) + '"\n')
			output.write('\t},\n')
		else:
			output.write('\t"from": {\n')
			output.write('\t},\n')

class Join():
	tables = []
	links = []

	def __init__(self):
		self.tables = []
		self.links = []

	def add_table(self, table):
		if table not in self.tables:
			self.tables.append(table)

	def set_links(self, links):
		self.links = links

	def get_tables(self):
		return self.tables

	def get_links(self):
		return self.links

	def __str__(self):
		if len(self.links) >= 1:
			string = ''
			for i in range(0, len(self.links)):
				string += ' ' + 'INNER JOIN ' + str(self.links[i][1][0]) + ' ' + 'ON ' + str(self.links[i][0][0]) + '.' + str(self.links[i][0][1]) + ' = ' + str(self.links[i][1][0]) + '.' + str(self.links[i][1][1])
			return string
		elif len(self.tables) >= 1:
			if len(self.tables) == 1:
				return ' ' + color.BOLD + 'NATURAL JOIN ' + color.END + self.tables[0]
			else:
				string = ' ' + color.BOLD + 'NATURAL JOIN ' + color.END
				for i in range(0, len(self.tables)):
					if i == (len(self.tables)-1):
						string += str(self.tables[i])
					else:
						string += str(self.tables[i]) + ', '
				return string
		else:
			return ''

	def print_json(self, output):
		if len(self.tables) >= 1:
			if len(self.tables) == 1:
				output.write('\t"join": {\n')
				output.write('\t\t"table": "' + str(self.tables[0]) + '"\n')
				output.write('\t},\n')
			else:
				output.write('\t"join": {\n')
				output.write('\t\t"tables": [')
				for i in range(0, len(self.tables)):
					if i == (len(self.tables)-1):
						output.write('"' + str(self.tables[i]) + '"')
					else:
						output.write('"' + str(self.tables[i]) + '", ')
				output.write(']\n')
				output.write('\t},\n')
		else:
			output.write('\t"join": {\n')
			output.write('\t},\n')

class Condition():
	column = ''
	column_type = ''
	operator = ''
	value = ''

	def __init__(self, column, column_type, operator, value):
		self.column = column
		self.column_type = column_type
		self.operator = operator
		self.value = value

	def get_column(self):
		return self.column

	def get_column_type(self):
		return self.column_type

	def get_operator(self):
		return self.operator

	def get_value(self):
		return self.value

	def get_in_list(self):
		return [self.column, self.column_type, self.operator, self.value]

	def get_just_column_name(self, column):
		if column != str(None):
			return column.rsplit('.', 1)[1]
		else:
			return column

	def get_column_with_type_operation(self, column, column_type):
		if column_type is None:
			return self.column
		else:
			return color.BOLD + str(column_type) + '(' + color.END + self.column + color.BOLD + ')' + color.END

	def get_pretty_operator(self, operator):
		if operator == 'BETWEEN':
			return color.BOLD + 'BETWEEN' + color.END + ' OOV ' + color.BOLD + 'AND' + color.END
		else:
			return color.BOLD + operator + color.END

	def __str__(self):
		return str(self.get_column_with_type_operation(self.column, self.column_type)) + ' ' + str(self.get_pretty_operator(self.operator)) + ' ' + str(self.value)

	def print_json(self, output):
		output.write('\t\t\t{ "column": "' + self.get_just_column_name(str(self.column)) + '",\n\t\t\t  "type": "' + str(self.column_type) + '",\n\t\t\t  "operator": "' + str(self.operator) + '",\n\t\t\t  "value": "' + str(self.value) + '"\n\t\t\t}')

class Where():
	conditions = []

	def __init__(self, clause=None):
		if clause is not None:
			self.conditions.append([None, clause])
		else:
			self.conditions = []

	def add_condition(self, junction, clause):
		self.conditions.append([junction, clause])

	def get_conditions(self):
		return self.conditions

	def __str__(self):
		string = ''
		if len(self.conditions) >= 1:
			for i in range(0, len(self.conditions)):
				if i == 0:
					string += ' ' + color.BOLD + 'WHERE' + color.END + ' ' + str(self.conditions[i][1])
				else:
					string += ' ' + color.BOLD + str(self.conditions[i][0]) + color.END + ' ' + str(self.conditions[i][1])
			return string
		else:
			return string

	def print_json(self, output):
		if len(self.conditions) >= 1:
			if len(self.conditions) == 1:
				output.write('\t"where": {\n')
				output.write('\t\t"condition": [\n')
				self.conditions[0][1].print_json(output)
				output.write('\n')
				output.write('\t\t]\n')
				output.write('\t},\n')
			else:
				output.write('\t"where": {\n')
				output.write('\t\t"conditions": [\n')
				for i in range(0, len(self.conditions)):
					if i != 0:
						output.write('\t\t\t{\n\t\t\t  "operator": "' + str(self.conditions[i][0]) + '"\n\t\t\t},\n')
					self.conditions[i][1].print_json(output)
					if i != (len(self.conditions)-1):
						output.write(',')
					output.write('\n')
				output.write('\t\t]\n')
				output.write('\t},\n')
		else:
			output.write('\t"where": {\n')
			output.write('\t},\n')
    
class GroupBy():
	column = None

	def __init__(self, column=None):
		if column is not None:
			self.column = column
		else:
			self.column = None

	def set_column(self, column):
		self.column = column

	def get_column(self):
		return self.column

	def get_just_column_name(self, column):
		if column != str(None):
			return column.rsplit('.', 1)[1]
		else:
			return column

	def __str__(self):
		if self.column is not None:
			return ' ' + color.BOLD + 'GROUP BY ' + color.END + str(self.column)
		else:
			return ''

	def print_json(self, output):
		if self.column is not None:
			output.write('\t"group_by": {\n')
			output.write('\t\t"column": "' + self.get_just_column_name(str(self.column)) + '"\n')
			output.write('\t},\n')
		else:
			output.write('\t"group_by": {\n')
			output.write('\t},\n')

class OrderBy():
	columns = []
	order = None

	def __init__(self, columns=None, order=None):
		if columns is not None:
			self.columns = columns
		else:
			self.columns = []

		if order is not None:
			self.order = order
		else:
			self.order = None

	def add_column(self, column):
		if column not in self.columns:
			self.columns.append(column)

	def get_columns(self):
		return self.columns

	def set_order(self, order):
		self.order = order

	def get_order(self):
		return self.order

	def get_just_column_name(self, column):
		if column != str(None):
			return column.rsplit('.', 1)[1]
		else:
			return column

	def __str__(self):
		if self.columns != []:
			string = color.BOLD + 'ORDER BY ' + color.END
			for i in range(0, len(self.columns)):
				if i == (len(self.columns)-1):
					string += self.columns[i]
				else:
					string += self.columns[i] + ', '
			if self.order == 0:
				string += color.BOLD + ' ASC' + color.END
			else:
				string += color.BOLD + ' ASC' + color.END
			return ' ' + string
		else:
			return ''

	def print_json(self, output):
		if len(self.columns) >= 1:
			if len(self.columns) == 1:
				output.write('\t"order_by": {\n')
				output.write('\t\t"order": "' + str(self.order) + '",\n')
				output.write('\t\t"column": "' + self.get_just_column_name(str(self.columns[0])) + '"\n')
				output.write('\t},\n')
			else:
				output.write('\t"order_by": {\n')
				output.write('\t\t"order": "' + str(self.order) + '",\n')
				output.write('\t\t"columns": [')
				for i in range(0, len(self.columns)):
					if i == (len(self.columns)-1):
						output.write('"' + self.get_just_column_name(str(self.columns[i])) + '"')
					else:
						output.write('"' + self.get_just_column_name(str(self.columns[i])) + '", ')
				output.write(']\n')
				output.write('\t},\n')
		else:
			output.write('\t"order_by": {\n')
			output.write('\t}\n')

class Query():
	select = None
	_from = None
	join = None
	where = None
	group_by = None
	order_by = None

	def __init__(self, select=None, _from=None, join=None, where=None, group_by=None, order_by=None):
		if select is not None:
			self.select = select
		else:
			self.select = None
		if _from is not None:
			self._from = _from
		else:
			self._from = None
		if join is not None:
			self.join = join
		else:
			self.join = None
		if where is not None:
			self.where = where
		else:
			self.where = None
		if group_by is not None:
			self.group_by = group_by
		else:
			self.group_by = None
		if order_by is not None:
			self.order_by = order_by
		else:
			self.order_by = None

	def set_select(self, select):
		self.select = select

	def get_select(self):
		return self.select

	def set_from(self, _from):
		self._from = _from

	def get_from(self):
		return self._from

	def set_join(self, join):
		self.join = join

	def get_join(self):
		return self.join

	def set_where(self, where):
		self.where = where

	def get_where(self):
		return self.where

	def set_group_by(self, group_by):
		self.group_by = group_by

	def get_group_by(self):
		return self.group_by

	def set_order_by(self, order_by):
		self.order_by = order_by

	def get_order_by(self):
		return self.order_by

	def __str__(self):
		return str(self.select) + str(self._from) + str(self.join) + str(self.where) + str(self.group_by) + str(self.order_by) + ';'

	def print_json(self, filename="output.json"):
		output = open(filename, 'a')
		output.write('{\n')
		self.select.print_json(output)
		self._from.print_json(output)
		self.join.print_json(output)
		self.where.print_json(output)
		self.group_by.print_json(output)
		self.order_by.print_json(output)
		output.write('}\n')
		output.close()


# In[70]:


# -*- coding: utf-8 -*

import sys
import unicodedata

imp.reload(sys)
#sys.setdefaultencoding("utf-8")

class ParsingException(Exception):
    reason = ''
    
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'Error: ' + self.reason


# In[80]:


from threading import Thread
class SelectParser(Thread):
    def __init__(self, columns_of_select, tables_of_from, phrase, count_keywords, sum_keywords, average_keywords, max_keywords, min_keywords, database_dico):
        Thread.__init__(self)
        self.select_objects = []
        self.columns_of_select = columns_of_select
        self.tables_of_from = tables_of_from
        self.phrase = phrase
        self.count_keywords = count_keywords
        self.sum_keywords = sum_keywords
        self.average_keywords = average_keywords
        self.max_keywords = max_keywords
        self.min_keywords = min_keywords
        self.database_dico = database_dico

    def get_tables_of_column(self, column):
        tmp_table = []
        for table in self.database_dico:
            if column in self.database_dico[table]:
                 tmp_table.append(table)
        return tmp_table

    def get_column_name_with_alias_table(self, column, table_of_from):
        one_table_of_column = self.get_tables_of_column(column)[0]
        tables_of_column = self.get_tables_of_column(column)
        if table_of_from in tables_of_column:
            return str(table_of_from) + '.' + str(column)
        else:
            return str(one_table_of_column) + '.' + str(column)

    def run(self):
        for table_of_from in self.tables_of_from:
            self.select_object = Select()
            is_count = False
            number_of_select_column = len(self.columns_of_select)

            if number_of_select_column == 0:
                for count_keyword in self.count_keywords:
                    if count_keyword in self.phrase:
                        is_count = True

                if is_count:
                    self.select_object.add_column(None, 'COUNT')
                else:
                    self.select_object.add_column(None, None)
            else:
                select_phrases = []
                previous_index = 0
                for i in range(0,len(self.phrase)):
                    if self.phrase[i] in self.columns_of_select:
                        select_phrases.append(self.phrase[previous_index:i+1])
                        previous_index = i+1

                select_phrases.append(self.phrase[previous_index:])

                for i in range(0, len(select_phrases)):
                    select_type = None
                    phrase = ' '.join(select_phrases[i])

                    for keyword in self.average_keywords:
                        if keyword in phrase:
                            select_type = 'AVG'
                    for keyword in self.count_keywords:
                        if keyword in phrase:
                            select_type = 'COUNT'
                    for keyword in self.max_keywords:
                        if keyword in phrase:
                            select_type = 'MAX'
                    for keyword in self.min_keywords:
                        if keyword in phrase:
                            select_type = 'MIN'
                    for keyword in self.sum_keywords:
                        if keyword in phrase:
                            select_type = 'SUM'

                    if (i != len(select_phrases)-1) or (select_type is not None):
                        if i >= len(self.columns_of_select):
                            column = None
                        else:
                        	column = self.get_column_name_with_alias_table(self.columns_of_select[i], table_of_from)
                        self.select_object.add_column(column, select_type)

            self.select_objects.append(self.select_object)


    def join(self):
        Thread.join(self)
        return self.select_objects


# In[81]:


class FromParser(Thread):
    def __init__(self, tables_of_from, columns_of_select, columns_of_where, database_object):
        Thread.__init__(self)
        self.queries = []
        self.tables_of_from = tables_of_from
        self.columns_of_select = columns_of_select
        self.columns_of_where = columns_of_where
        
        self.database_object = database_object
        self.database_dico = self.database_object.get_tables_into_dictionnary()

    def get_tables_of_column(self, column):
        tmp_table = []
        for table in self.database_dico:
            if column in self.database_dico[table]:
                 tmp_table.append(table)
        return tmp_table

    def intersect(self, a, b):
        return list(set(a) & set(b))

    def find_fk(self, a, b):
        pass

    def difference(self, a, b):
        differences = []
        for _list in a:
            if _list not in b:
               differences.append(_list)
        return differences

    def is_direct_join_is_possible(self, table_src, table_trg):
        # pk_table_src = self.database_object.get_primary_keys_of_table(table_src)
        # pk_table_trg = self.database_object.get_primary_keys_of_table(table_trg)
        # match_pk_table_src_with_table_trg = self.intersect(pk_table_src, self.database_dico[table_trg])
        # match_pk_table_trg_with_table_src = self.intersect(pk_table_trg, self.database_dico[table_src])
        
        # if len(match_pk_table_src_with_table_trg) >=1:
        #     return [table_src, match_pk_table_src_with_table_trg[0], table_trg]
        # elif len(match_pk_table_trg_with_table_src) >= 1:
        #     return [table_src, match_pk_table_trg_with_table_src[0], table_trg]



        fk_table_src = self.database_object.get_foreign_keys_of_table(table_src)
        fk_table_trg = self.database_object.get_foreign_keys_of_table(table_trg)

        for fk_dict in fk_table_src:
            if fk_dict['ref_table'] == table_trg:
                return [(table_src,fk_dict['col']), (table_trg,fk_dict['ref_col'])]

        for fk_dict in fk_table_trg:
            if fk_dict['ref_table'] == table_src:
                return [(table_trg,fk_dict['col']), (table_src, fk_dict['ref_col'])]

    def get_all_direct_linked_tables_of_a_table(self, table_src):
        links = []
        for table_trg in self.database_dico:
            if table_trg != table_src:
                link = self.is_direct_join_is_possible(table_src, table_trg)
                if link is not None:
                    links.append(link)
        return links

    def is_join(self, historic, table_src, table_trg):
        historic = historic
        links = self.get_all_direct_linked_tables_of_a_table(table_src)

        differences = []
        for join in links:
            if join[1][0] not in historic:
                differences.append(join)
        links = differences 

        for join in links:
            if join[1][0] == table_trg:
                return [0, join]

        path = []
        historic.append(table_src)

        for join in links:
            result = [1, self.is_join(historic, join[1][0], table_trg)]
            if result[1] != []:
                if result[0] == 0:
                    path.append(result[1])
                    path.append(join)
                else:
                    path = result[1]
                    path.append(join)
        return path

    def get_link(self, table_src, table_trg):
        path = self.is_join([], table_src, table_trg)
        if len(path) > 0:
            path.pop(0)
            path.reverse()
        return path

    def unique(self, _list):
        return [list(x) for x in set(tuple(x) for x in _list)]

    def unique_ordered(self, _list):
        frequency = []
        for element in _list:
            if element not in frequency:
                frequency.append(element)
        return frequency


    def run(self):
        self.queries = []

        for table_of_from in self.tables_of_from:
            links = []
            query = Query()
            query.set_from(From(table_of_from))
            join_object = Join()
            for column in self.columns_of_select:
                if column not in self.database_dico[table_of_from]:
                    foreign_table = self.get_tables_of_column(column)[0]
                    join_object.add_table(foreign_table)
                    link = self.get_link(table_of_from, foreign_table)
                    links.extend(link)
            for column in self.columns_of_where:
                if column not in self.database_dico[table_of_from]:
                    foreign_table = self.get_tables_of_column(column)[0]
                    join_object.add_table(foreign_table)
                    link = self.get_link(table_of_from, foreign_table)
                    links.extend(link)

            join_object.set_links(self.unique_ordered(links))
            query.set_join(join_object)
            self.queries.append(query)
            if len(join_object.get_tables()) > len(join_object.get_links()):
                self.queries = None

    def join(self):
        Thread.join(self)
        return self.queries


# In[87]:


class WhereParser(Thread):
    def __init__(self, phrases, tables_of_from, count_keywords, sum_keywords, average_keywords, max_keywords, min_keywords, greater_keywords, less_keywords, between_keywords, negation_keywords, junction_keywords, disjunction_keywords, database_dico, columns_of_values_of_where):
        Thread.__init__(self)
        self.where_objects = []
        self.phrases = phrases
        self.tables_of_from = tables_of_from
        self.count_keywords = count_keywords
        self.sum_keywords = sum_keywords
        self.average_keywords = average_keywords
        self.max_keywords = max_keywords
        self.min_keywords = min_keywords
        self.greater_keywords = greater_keywords
        self.less_keywords = less_keywords
        self.between_keywords = between_keywords
        self.negation_keywords = negation_keywords
        self.junction_keywords = junction_keywords
        self.disjunction_keywords = disjunction_keywords
        self.database_dico = database_dico
        # -----------------------------------------------

        self.columns_of_values_of_where = columns_of_values_of_where

        # -----------------------------------------------

    def get_tables_of_column(self, column):
        tmp_table = []
        for table in self.database_dico:
            if column in self.database_dico[table]:
                 tmp_table.append(table)
        return tmp_table

    def get_column_name_with_alias_table(self,column, table_of_from):
        one_table_of_column = self.get_tables_of_column(column)[0]
        tables_of_column = self.get_tables_of_column(column)
        if table_of_from in tables_of_column:
            return str(table_of_from) + '.' + str(column)
        else:
            return str(one_table_of_column) + '.' + str(column)

    def intersect(self, a, b):
        return list(set(a) & set(b))

    def predict_operation_type(self, previous_column_offset, current_column_offset):
        interval_offset = range(previous_column_offset, current_column_offset)
        if(len(self.intersect(interval_offset, self.count_keyword_offset)) >= 1):
            return 'COUNT'
        elif(len(self.intersect(interval_offset, self.sum_keyword_offset)) >= 1):
            return 'SUM'
        elif(len(self.intersect(interval_offset, self.average_keyword_offset)) >= 1):
            return 'AVG'
        elif(len(self.intersect(interval_offset, self.max_keyword_offset)) >= 1):
            return 'MAX'
        elif(len(self.intersect(interval_offset, self.min_keyword_offset)) >= 1):
            return 'MIN'
        else:
            return None

    def predict_operator(self, current_column_offset, next_column_offset):
        interval_offset = range(current_column_offset, next_column_offset)
        if(len(self.intersect(interval_offset, self.negation_keyword_offset)) >= 1) and (len(self.intersect(interval_offset, self.greater_keyword_offset)) >= 1):
            return '<'
        elif(len(self.intersect(interval_offset, self.negation_keyword_offset)) >= 1) and (len(self.intersect(interval_offset, self.less_keyword_offset)) >= 1):
            return '>'
        if(len(self.intersect(interval_offset, self.less_keyword_offset)) >= 1):
            return '<'
        elif(len(self.intersect(interval_offset, self.greater_keyword_offset)) >= 1):
            return '>'
        elif(len(self.intersect(interval_offset, self.between_keyword_offset)) >= 1):
            return 'BETWEEN'
        elif(len(self.intersect(interval_offset, self.negation_keyword_offset)) >= 1):
            return '!='
        else:
            return '='

    def predict_junction(self, previous_column_offset, current_column_offset):
        interval_offset = range(previous_column_offset, current_column_offset)
        junction = 'AND'
        if(len(self.intersect(interval_offset, self.disjunction_keyword_offset)) >= 1):
            return 'OR'
        elif(len(self.intersect(interval_offset, self.junction_keyword_offset)) >= 1):
            return 'AND'

        first_encountered_junction_offset = -1
        first_encountered_disjunction_offset = -1

        for offset in self.junction_keyword_offset:
            if offset >= current_column_offset:
                first_encountered_junction_offset = offset
                break

        for offset in self.disjunction_keyword_offset:
            if offset >= current_column_offset:
                first_encountered_disjunction_offset = offset
                break

        if first_encountered_junction_offset >= first_encountered_disjunction_offset:
            return 'AND'
        else: 
            return 'OR'

    def run(self):
        number_of_where_columns = 0
        columns_of_where = []
        offset_of = {}
        column_offset = []
        self.count_keyword_offset = []
        self.sum_keyword_offset = []
        self.average_keyword_offset = []
        self.max_keyword_offset = []
        self.min_keyword_offset = []
        self.greater_keyword_offset = []
        self.less_keyword_offset = []
        self.between_keyword_offset = []
        self.junction_keyword_offset = []
        self.disjunction_keyword_offset = []
        self.negation_keyword_offset = []

        for phrase in self.phrases:
            for i in range(0, len(phrase)):
                for table in self.database_dico:
                    if phrase[i] in self.database_dico[table]:
                        number_of_where_columns += 1
                        columns_of_where.append(phrase[i])
                        offset_of[phrase[i]] = i
                        column_offset.append(i)
                        break
                if phrase[i] in self.count_keywords: # before the column
                    self.count_keyword_offset.append(i)
                if phrase[i] in self.sum_keywords: # before the column
                    self.sum_keyword_offset.append(i)
                if phrase[i] in self.average_keywords: # before the column
                    self.average_keyword_offset.append(i)
                if phrase[i] in self.max_keywords: # before the column
                    self.max_keyword_offset.append(i)
                if phrase[i] in self.min_keywords: # before the column
                    self.min_keyword_offset.append(i)
                if phrase[i] in self.greater_keywords: # after the column
                    self.greater_keyword_offset.append(i)
                if phrase[i] in self.less_keywords: # after the column
                    self.less_keyword_offset.append(i)
                if phrase[i] in self.between_keywords: # after the column
                    self.between_keyword_offset.append(i)
                if phrase[i] in self.junction_keywords: # after the column
                    self.junction_keyword_offset.append(i)
                if phrase[i] in self.disjunction_keywords: # after the column
                    self.disjunction_keyword_offset.append(i)
                if phrase[i] in self.negation_keywords: # between the column and the equal, greater or less keyword
                    self.negation_keyword_offset.append(i)

        for table_of_from in self.tables_of_from:
            where_object = Where()
            
            for i in range(0, len(column_offset)):
                current = column_offset[i]
                if (i==0):
                    previous = 0
                else:
                    previous = column_offset[i-1]

                if i == (len(column_offset) - 1):
                    _next = 100 # put max integer in python here ?
                else:
                    _next = column_offset[i+1]

                junction = self.predict_junction(previous, current)
                column = self.get_column_name_with_alias_table(columns_of_where[i], table_of_from)
                operation_type = self.predict_operation_type(previous, current)
                
                if len(self.columns_of_values_of_where) >= len(columns_of_where):                   
                    value = self.columns_of_values_of_where[i]
                else:
                    value = 'OOV' # Out Of Vocabulary: feature not implemented yet

                # -----------------------------------------------
                    
                operator = self.predict_operator(current, _next)
                where_object.add_condition(junction, Condition(column, operation_type, operator, value))
            self.where_objects.append(where_object)

    def join(self):
        Thread.join(self)
        return self.where_objects


# In[126]:


class GroupByParser(Thread):
    def __init__(self, phrases, tables_of_from, database_dico):
        Thread.__init__(self)
        self.group_by_objects = []
        self.phrases = phrases
        self.tables_of_from = tables_of_from
        self.database_dico = database_dico

    def get_tables_of_column(self, column):
        tmp_table = []
        for table in self.database_dico:
            if column in self.database_dico[table]:
                 tmp_table.append(table)
        return tmp_table

    def get_column_name_with_alias_table(self, column, table_of_from):
        one_table_of_column = self.get_tables_of_column(column)[0]
        tables_of_column = self.get_tables_of_column(column)
        if table_of_from in tables_of_column:
            return str(table_of_from) + '.' + str(column)
        else:
            return str(one_table_of_column) + '.' + str(column)

    def run(self):
        for table_of_from in self.tables_of_from:
            group_by_object = GroupBy()
            for phrase in self.phrases:
                for i in range(0, len(phrase)):
                    for table in self.database_dico:
                        if phrase[i] in self.database_dico[table]:
                            column = self.get_column_name_with_alias_table(phrase[i], table_of_from)
                            group_by_object.set_column(column)
            self.group_by_objects.append(group_by_object)

    def join(self):
        Thread.join(self)
        return self.group_by_objects

class OrderByParser(Thread):
    def __init__(self, phrases, tables_of_from, database_dico):
        Thread.__init__(self)
        self.order_by_objects = []
        self.phrases = phrases
        self.tables_of_from = tables_of_from
        self.database_dico = database_dico

    def get_tables_of_column(self, column):
        tmp_table = []
        for table in self.database_dico:
            if column in self.database_dico[table]:
                 tmp_table.append(table)
        return tmp_table

    def get_column_name_with_alias_table(self, column, table_of_from):
        one_table_of_column = self.get_tables_of_column(column)[0]
        tables_of_column = self.get_tables_of_column(column)
        if table_of_from in tables_of_column:
            return str(table_of_from) + '.' + str(column)
        else:
            return str(one_table_of_column) + '.' + str(column)

    def run(self):
        for table_of_from in self.tables_of_from:
            order_by_object = OrderBy()
            for phrase in self.phrases:
                for i in range(0, len(phrase)):
                    for table in self.database_dico:
                        if phrase[i] in self.database_dico[table]:
                            column = self.get_column_name_with_alias_table(phrase[i], table_of_from)
                            order_by_object.add_column(column)
            order_by_object.set_order(0)
            self.order_by_objects.append(order_by_object)

    def join(self):
        Thread.join(self)
        return self.order_by_objects

class Parser:
    database_object = None
    database_dico = None
    language = None
    thesaurus_object = None

    count_keywords = []
    sum_keywords = []
    average_keywords = []
    max_keywords = []
    min_keywords = []
    junction_keywords = []
    disjunction_keywords = []
    greater_keywords = []
    less_keywords = []
    between_keywords = []
    order_by_keywords = []
    group_by_keywords = []
    negation_keywords = []

    def __init__(self, database, config):
        self.database_object = database
        self.database_dico = self.database_object.get_tables_into_dictionnary()

        self.count_keywords = config.get_count_keywords()
        self.sum_keywords = config.get_sum_keywords()
        self.average_keywords = config.get_avg_keywords()
        self.max_keywords = config.get_max_keywords()
        self.min_keywords = config.get_min_keywords()
        self.junction_keywords = config.get_junction_keywords()
        self.disjunction_keywords = config.get_disjunction_keywords()
        self.greater_keywords = config.get_greater_keywords()
        self.less_keywords = config.get_less_keywords()
        self.between_keywords = config.get_between_keywords()
        self.order_by_keywords = config.get_order_by_keywords()
        self.group_by_keywords = config.get_group_by_keywords()
        self.negation_keywords = config.get_negation_keywords()

    def set_thesaurus(self, thesaurus):
        self.thesaurus_object = thesaurus

    def remove_accents(self, string):
        nkfd_form = unicodedata.normalize('NFKD', str(string))
        return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

    def parse_sentence(self, sentence):
        number_of_table = 0
        number_of_select_column = 0
        number_of_where_column = 0
        last_table_position = 0
        columns_of_select = []
        columns_of_where = []
        
        # ---------------------------------------------------------------------

        input_for_finding_value=sentence
        columns_of_values_of_where=[]

        filter_list=[",","!"]

        for filter_element in filter_list:
            input_for_finding_value=input_for_finding_value.replace(filter_element," ")

        input_word_list=input_for_finding_value.split()
        
        # print "asd -> ",input_word_list    


        #===    clause extractor


        number_of_where_column_temp = 0
        number_of_table_temp = 0
        last_table_position_temp = 0
        start_phrase = ''
        med_phrase = ''
        end_phrase = ''

        for i in range(0, len(input_word_list)):            
            if input_word_list[i] in self.database_dico:
                if number_of_table_temp == 0:
                    start_phrase = input_word_list[:i]
                number_of_table_temp+=1
                last_table_position_temp = i
            for table in self.database_dico:
                if input_word_list[i] in self.database_dico[table]:
                    if number_of_where_column_temp == 0:
                        med_phrase = input_word_list[len(start_phrase):last_table_position_temp+1]
                    number_of_where_column_temp+=1
                    break
                else:
                    if (number_of_table_temp != 0) and (number_of_where_column_temp == 0) and (i == (len(input_word_list)-1)):
                        med_phrase = input_word_list[len(start_phrase):]

        end_phrase = input_word_list[len(start_phrase) + len(med_phrase):]
        irext = ' '.join(end_phrase)
        # print 'irext :',irext


        #===       

        # condition_str_where='where'
        # exist_check_where=sentence.find(condition_str_where)

        # condition_str_for='for'
        # exist_check_for=sentence.find(condition_str_for)
        # if exist_check_where != -1 or exist_check_for != -1:

        if irext :

            # print "entered"

            # if  exist_check_where != -1 :   
            #     irext=sentence.split(condition_str_where)[1]   
            # else :
            #     irext=sentence.split(condition_str_for)[1]     

            mirext=irext.lower()
           
            # print "-----"
            # print "sentence : ",sentence
            # print "irext : ",irext            
            # print "-----"

            filter_list=[",","!"]

            for filter_element in filter_list:
                irext=irext.replace(filter_element," ")

            assignment_list=[" equals to "," equal to ","="," is ",":"," equals "," equal "," than "]
            maverickjoy_assigner_convention ="res@3#>>"
            
            for assigners in assignment_list :
                irext=irext.replace(assigners," res@3#>> ")
                # print "ire : ",irext        
            # print 'irext:',irext
        

            # replace all spaces from values to <_> for proper value assignment in SQL
            # eg. (where name is 'abc def') -> (where name is abc<_>def)
            for i in re.findall("('.*?')",irext):
                irext = irext.replace(i,i.replace(' ','<_>').replace("'",''))

            irext_list = irext.split()
            # print "ire : ",irext_list

            index_list_values=[(i+1) for i,x in enumerate(irext_list) if x == maverickjoy_assigner_convention]
            # print "ilv : ",index_list_values

            for index in index_list_values:
                if index < len(irext_list):
                    # replace back <_> to spaces from the values assigned
                    columns_of_values_of_where.append(str("'"+str(irext_list[index]).replace('<_>',' ')+"'"))      

            # print " = > ",columns_of_values_of_where   


        # ---------------------------------------------------------------------
        
        tables_of_from = []
        select_phrase = ''
        from_phrase = ''
        where_phrase = ''
        
        words = re.findall(r"[\w]+", self.remove_accents(sentence))

        for i in range(0, len(words)):            
            if words[i] in self.database_dico:
                if number_of_table == 0:
                    select_phrase = words[:i]
                tables_of_from.append(words[i])
                number_of_table+=1
                last_table_position = i
            for table in self.database_dico:
                if words[i] in self.database_dico[table]:
                    if number_of_table == 0:
                        columns_of_select.append(words[i])
                        number_of_select_column+=1
                    else:
                        if number_of_where_column == 0:
                            from_phrase = words[len(select_phrase):last_table_position+1]
                        columns_of_where.append(words[i])
                        number_of_where_column+=1
                    break
                else:
                    if (number_of_table != 0) and (number_of_where_column == 0) and (i == (len(words)-1)):
                        from_phrase = words[len(select_phrase):]

        where_phrase = words[len(select_phrase) + len(from_phrase):]

        # print "where => ", where_phrase
        
        if (number_of_select_column + number_of_table + number_of_where_column) == 0:
            raise ParsingException("No keyword found in sentence!")

        if len(tables_of_from) > 0:
            from_phrases = []
            previous_index = 0
            for i in range(0,len(from_phrase)):
                if from_phrase[i] in tables_of_from:
                    from_phrases.append(from_phrase[previous_index:i+1])
                    previous_index = i+1

            last_junction_word_index = -1

            for i in range(0, len(from_phrases)):
                number_of_junction_words = 0
                number_of_disjunction_words = 0

                for word in from_phrases[i]:
                    if word in self.junction_keywords:
                        number_of_junction_words += 1
                    if word in self.disjunction_keywords:
                        number_of_disjunction_words += 1

                if (number_of_junction_words + number_of_disjunction_words) > 0:
                    last_junction_word_index = i

            if last_junction_word_index == -1:
                from_phrase = sum(from_phrases[:1], [])
                where_phrase = sum(from_phrases[1:], []) + where_phrase
            else:
                 from_phrase = sum(from_phrases[:last_junction_word_index+1], [])
                 where_phrase = sum(from_phrases[last_junction_word_index+1:], []) + where_phrase

        real_tables_of_from = []

        for word in from_phrase:
            if word in tables_of_from:
                real_tables_of_from.append(word)
        tables_of_from = real_tables_of_from

        if len(tables_of_from) == 0:
            raise ParsingException("No table name found in sentence!")

        group_by_phrase = []
        order_by_phrase = []
        new_where_phrase = []
        previous_index = 0
        previous_phrase_type = 0
        yet_where = 0

        for i in range(0, len(where_phrase)):
            if where_phrase[i] in self.order_by_keywords:
                if yet_where > 0:
                    if previous_phrase_type == 1:
                        order_by_phrase.append(where_phrase[previous_index:i])
                    elif previous_phrase_type == 2:
                        group_by_phrase.append(where_phrase[previous_index:i])
                else:
                    new_where_phrase.append(where_phrase[previous_index:i])
                previous_index = i
                previous_phrase_type = 1
                yet_where += 1
            if where_phrase[i] in self.group_by_keywords:
                if yet_where > 0:
                    if previous_phrase_type == 1:
                        order_by_phrase.append(where_phrase[previous_index:i])
                    elif previous_phrase_type == 2:
                        group_by_phrase.append(where_phrase[previous_index:i])
                else:
                    new_where_phrase.append(where_phrase[previous_index:i])
                previous_index = i
                previous_phrase_type = 2
                yet_where += 1

        if previous_phrase_type == 1:
            order_by_phrase.append(where_phrase[previous_index:])
        elif previous_phrase_type == 2:
            group_by_phrase.append(where_phrase[previous_index:])
        else:
            new_where_phrase.append(where_phrase)
        
        select_parser = SelectParser(columns_of_select, tables_of_from, select_phrase, self.count_keywords, self.sum_keywords, self.average_keywords, self.max_keywords, self.min_keywords, self.database_dico)
        from_parser = FromParser(tables_of_from, columns_of_select, columns_of_where, self.database_object)
        where_parser = WhereParser(new_where_phrase, tables_of_from, self.count_keywords, self.sum_keywords, self.average_keywords, self.max_keywords, self.min_keywords, self.greater_keywords, self.less_keywords, self.between_keywords, self.negation_keywords, self.junction_keywords, self.disjunction_keywords, self.database_dico, columns_of_values_of_where)
        group_by_parser = GroupByParser(group_by_phrase, tables_of_from, self.database_dico)
        order_by_parser = OrderByParser(order_by_phrase, tables_of_from, self.database_dico)

        select_parser.start()
        from_parser.start()
        where_parser.start()
        group_by_parser.start()
        order_by_parser.start()

        queries = from_parser.join()



        if queries is None:
            raise ParsingException("There is at least one unattainable column from the table of FROM!")

        select_objects = select_parser.join()
        where_objects = where_parser.join()
        group_by_objects = group_by_parser.join()
        order_by_objects = order_by_parser.join()

        for i in range(0, len(queries)):
            query = queries[i]
            query.set_select(select_objects[i])
            query.set_where(where_objects[i])
            query.set_group_by(group_by_objects[i])
            query.set_order_by(order_by_objects[i])

        return queries


# In[91]:


#!/usr/bin/python
# -*- coding: utf-8 -*

import os, sys, getopt
import unicodedata



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class ln2sql:
    def __init__(self, database_path, input_sentence, language_path, thesaurus_path, json_output_path):
        database = Database()
        database.load(database_path)
        #database.print_me()

        config = LangConfig()
        config.load(language_path)

        parser = Parser(database, config)

        if thesaurus_path is not None:
            thesaurus = Thesaurus()
            thesaurus.load(thesaurus_path)
            parser.set_thesaurus(thesaurus)

        queries = parser.parse_sentence(input_sentence)

        if json_output_path is not None:
            self.remove_json(json_output_path)
            for query in queries:
                query.print_json(json_output_path)

        if(len(queries) > 1):
            if settings.DEBUG :
                print('--------- queries is more than one')
            self.query = None

            raise Exception('More than one query')
        else :
            self.query = queries[0]

        if settings.DEBUG :
            for query in queries:
                print (query)

    def getQuery(self):
        return self.query

    def remove_json(self, filename="output.json"):
        if os.path.exists(filename):
            os.remove(filename)

def print_help_message():
    if settings.DEBUG :
        print ('\n')
        print ('Usage:')
        print ('\tpython ln2sql.py -d <path> -l <path> -i <input-sentence> [-t <path>] [-j <path>]')
        print ('Parameters:')
        print ('\t-h\t\t\tprint this help message')
        print ('\t-d <path>\t\tpath to SQL dump file')
        print ('\t-l <path>\t\tpath to language configuration file')
        print ('\t-i <input-sentence>\tinput sentence to parse')
        print ('\t-j <path>\t\tpath to JSON output file')
        print ('\t-t <path>\t\tpath to thesaurus file')
        print ('\n')

def main(argv):
    # try:
    opts, args = getopt.getopt(argv,"d:l:i:t:j:")
    database_path = None
    input_sentence = None
    language_path = None
    thesaurus_path = None
    json_output_path = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-d":
            database_path = opts[i][1]
        elif opts[i][0] == "-l":
            language_path = opts[i][1]
        elif opts[i][0] == "-i":
            input_sentence = opts[i][1]
        elif opts[i][0] == "-j":
            json_output_path = opts[i][1]
        elif opts[i][0] == "-t":
            thesaurus_path = opts[i][1]
        else:
            print_help_message()
            # sys.exit()
            raise getopt.GetoptError('ln2sqlmodule : Invalid args received',None)
    
    if (database_path is None) or (input_sentence is None) or (language_path is None):
        raise getopt.GetoptError('ln2sqlmodule : Invalid args received',None)
    else:
        if thesaurus_path is not None:
            thesaurus_path = str(thesaurus_path)
        if json_output_path is not None:
            json_output_path = str(json_output_path)

    #try:
    ln2sqlObj = ln2sql(str(database_path), str(input_sentence), str(language_path), thesaurus_path, json_output_path)
    
    return ln2sqlObj.getQuery()
    #except Exception, e:
    #    print color.BOLD + color.RED + str(e) + color.END

    # except getopt.GetoptError:
    #     print_help_message()


# if __name__ == '__main__':
#     main(sys.argv[1:])


# In[93]:


import unittest
#import __init__ as ln2sqlmodule


class Testln2sql(unittest.TestCase):

    def test_getSql(self):
        tests = [
            {
                "input": "emp",
                "output": "SELECT * FROM emp;"
            },
            {
                "input": "name of all emp",
                "output": "SELECT emp.name FROM emp;"
            },
            {
                "input": "name and score for emp with id = 2",
                "output": "SELECT emp.name, emp.score FROM emp WHERE emp.id = '2';"
            },
            {
                "input": "all data for city where cityName = 'pune'",
                "output": "SELECT * FROM city WHERE city.cityName = 'pune';"  
            },
            {
                "input": "cityName for emp",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id;"
            },
            {
                "input": "cityName for emp with id = 2",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.id = '2';"
            },
            {
                "input": "cityName and score for emp with id = 2",
                "output": "SELECT city.cityName, emp.score FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.id = '2';"
            },

        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql(test['input'],'emp.sql')), test['output'])

    def test_getSql_like(self):
        tests = [
            {
                "input": "emp",
                "output": "SELECT * FROM emp;"
            },
            {
                "input": "name of all emp",
                "output": "SELECT emp.name FROM emp;"
            },
            {
                "input": "name and score for emp with name = rupinder",
                "output": "SELECT emp.name, emp.score FROM emp WHERE emp.name LIKE '%rupinder%';"
            },
            {
                "input": "all data for city where cityName is 'pune'",
                "output": "SELECT * FROM city WHERE city.cityName LIKE '%pune%';"  
            },
            {
                "input": "cityName for emp",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id;"
            },
            {
                "input": "cityName for emp with name is 'rupinder singh'",
                "output": "SELECT city.cityName FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.name LIKE '%rupinder%singh%';"
            },
            {
                "input": "cityName and score for emp with score = 2",
                "output": "SELECT city.cityName, emp.score FROM emp INNER JOIN city ON emp.cityId = city.id WHERE emp.score LIKE '%2%';"
            }
        ]

        for test in tests:
            self.assertEqual(
                str(ln2sqlmodule.getSql_like(test['input'],'emp.sql')), test['output'])

if __name__ == '__main__':
    unittest.main()


# In[112]:


class SelectGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return

class FromGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return self.queries

class WhereGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return

class JoinGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return

class GroupByGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return

class OrderByGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        return

    def join(self):
        Thread.join(self)
        return

class Generator:

    def __init__(self):
        return

    def generate(self, queries):
        for query in queries:
            select_object = query.get_select()
            from_object = query.get_from()
            where_object = query.get_where()
            join_object = query.get_join()
            group_by_object = query.get_group_by()
            order_by_object = query.get_order_by()

            select_generator = SelectGenerator(select_object)
            from_generator = FromGenerator(from_object)
            where_generator = WhereGenerator(where_object)
            join_generator = JoinGenerator(join_object)
            group_by_generator = GroupByGenerator(group_by_object)
            order_by_generator = OrderByGenerator(order_by_object)

            select_generator.start()
            from_generator.start()
            where_generator.start()
            join_generator.start()
            group_by_generator.start()
            order_by_generator.start()

            select_phrase = select_generator.join()
            from_phrase = from_generator.join()
            where_phrase = where_generator.join()
            join_phrase = join_generator.join()
            group_by_phrase = group_by_generator.join()
            order_by_phrase = order_by_generator.join()


# In[ ]:





# In[110]:


def getSql(query, sqlDump, outputFile=None):
    # unit test
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', '-l', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json','-x']
    # args = ['-d', 'ln2sqlmodule/emp_dump.sql', 'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

    # args = ['-d', 'ln2sqlmodule/timesheet.sql', '-l',
    #         'ln2sqlmodule/lang/english.csv', '-i', query, '-j', 'ln2sqlmodule/output.json']

        args = ['-d', sqlDump,
                '-l', "C:/Users/Ishita_J/AppData/Local/Continuum/anaconda3/Lib/site-packages/ln2sqlmodule/lang/english.csv",
                '-i', query,
                '-j', outputFile]

        sql = main(args)

        return str(sql)


def getSql_like(query, sqlDump, outputFile=None):
        sql = getSql(query, sqlDump, outputFile)

        sql = re.sub("(WHERE \S+ )=", r'\g<1>LIKE', sql)
        sql = re.sub("(AND \S+ )=", r'\g<1>LIKE', sql)
        sql = re.sub("(OR \S+ )=", r'\g<1>LIKE', sql)

        # 'abc def' -> '%abc%def%'
        for i in re.findall("'(.*?)'", sql):
            sql = sql.replace(i, "%" + i + "%")
            sql = sql.replace(i, i.replace(' ', '%'))

        return sql


# In[102]:


# -*- coding: utf-8 -*

import sys
import unicodedata



class ParsingException(Exception):
    reason = ''
    
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'ParsingException : ' + self.reason

class GeneratingException(Exception):
    reason = ''

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'GeneratingException : ' + self.reason


# In[130]:


s = getSql("get count of all emp","C:/Users/Ishita_J/Desktop/emp.sql")


# In[129]:


getSql_like("get count of all emp","C:/Users/Ishita_J/Desktop/emp.sql")


# In[136]:


import re
print (re.sub('\x1b.*?m', '', s))


# In[137]:


s = getSql("get name of all emp","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[139]:


s = getSql("get name of all emp where score = 10 ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[141]:


s = getSql("what is the name in emp whose score is 10 ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[144]:


s = getSql("what is the name in emp whose score is 10 and cityId is pune ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[145]:


s = getSql("what is the number of emp with cityId pune ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[147]:


s = getSql("what is the maximum id in emp ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[149]:


s = getSql("what is the name of emp where id = maximum of emp id ","C:/Users/Ishita_J/Desktop/emp.sql")
print (re.sub('\x1b.*?m', '', s))


# In[ ]:




