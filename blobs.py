#!/usr/bin/env python

import argparse
import sys

def argParser():
    parser = argparse.ArgumentParser(description='Blobs')

    parser.add_argument('-i', '--input',
                       help='Input a file',
                       type=str,
                       default='input.txt')
    return vars(parser.parse_args())

def main():
    args = argParser()
    input_file = args['input']

    file_data = BuildArray(input_file)
    file_contents = file_data.get_file_contents()
    input_dict = file_data.get_data()

    find_cells = FindCells(input_dict)
    find_cells.locate_blob()
    read_count = find_cells.get_read_count()
    edges = find_cells.get_location()

    p = PrintAnswer(file_contents, edges, read_count)

class BuildArray():
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_dict = {}
        self.file_contents = []
        self._read_file()

    def _read_file(self):
        file = open(self.input_file)
        hash = 0
        for line in file:
            # Save file_contents for printing later
            self.file_contents.append(line.rstrip('\n'))
            line = line.rstrip('\n')
            for c in line:
                self.input_dict[hash] = [c, "new"]
                hash += 1
        file.close()

    def get_file_contents(self):
        return self.file_contents

    def get_data(self):
        return self.input_dict

class FindCells():
    def __init__(self, d):
        self.input_dict = d
        self.current_pos = {'row': 0, 'col': 0}
        self.location = {'top': 10, 'bottom': 0, 'left': 10, 'right': 0}
        self.read_count = 0

    def locate_blob(self):
        for key in self.input_dict:
            if self.input_dict[key][0] == '1':
                self.search_grid(key)

    def search_grid(self, key):
        self.update_pos(key)
        self.read_count += 1
        # Left
        try:
            if self.check_blob(key-1):
                if self.location['left'] > self.current_pos['col']:
                    self.location['left'] = self.current_pos['col']
                self.search_grid(key-1)
        except KeyError:
            # Caught the left edge
            pass
        # Down
        try:
            if self.check_blob(key+10):
                if self.location['bottom'] < self.current_pos['row']:
                    self.location['bottom'] = self.current_pos['row']
                self.search_grid(key+10)
        except KeyError:
            # Caught the bottom edge
            pass
        # Right
        try:
            if self.check_blob(key+1):
                if self.location['right'] < self.current_pos['col']:
                    self.location['right'] = self.current_pos['col']
                self.search_grid(key+1)
        except KeyError:
            # Caught the right edge
            pass
        # Up
        try:
            if self.check_blob(key-10):
                if self.location['top'] > self.current_pos['row']:
                    self.location['top'] = self.current_pos['row']
                self.search_grid(key-10)
        except KeyError:
            # Caught the top edge
            pass

        # The outer edges of the blob needs to be checked
        self.edge_location_update()
        return

    def get_location(self):
        return self.location

    def get_read_count(self):
        return self.read_count

    def edge_location_update(self):
        # Left
        if self.location['left'] > self.current_pos['col']:
            self.location['left'] = self.current_pos['col']
        # Down
        if self.location['bottom'] < self.current_pos['row']:
            self.location['bottom'] = self.current_pos['row']
        # Right
        if self.location['right'] < self.current_pos['col']:
            self.location['right'] = self.current_pos['col']
        # Up
        if self.location['top'] > self.current_pos['row']:
            self.location['top'] = self.current_pos['row']

    def check_blob(self, key):
        blob = False
        if self.input_dict[key][0] == '1' and \
           self.input_dict[key][1] == "new":
            blob = True
            self.input_dict[key][1] = "old"
        return blob

    def update_pos(self, key):
        if key == 0:
            self.current_pos['row'] = 0
        else:
            row = int(key/10)
            self.current_pos['row'] = row

        col = key % 10
        self.current_pos['col'] = col

class PrintAnswer():

    def __init__(self, input_file, edges, cells_read):
        self.input_file = input_file
        self.edges = edges
        self.cells_read = cells_read
        self._print_results()

    def _print_results(self):
        print "Sample input:"
        for i in self.input_file:
            print i

        print "\nSample Output:"
        print 'Cell Reads: %s' % self.cells_read
        print "Top: %s" % self.edges['top']
        print "Left: %s" % self.edges['left']
        print "Bottom: %s" % self.edges['bottom']
        print "Right: %s" % self.edges['right']

if __name__ == "__main__":
    sys.exit(main())
