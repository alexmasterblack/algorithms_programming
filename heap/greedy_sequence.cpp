#include <vector>
#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int, int> value_index;

bool comp(value_index element_one, value_index element_two) {
    if (element_one.second == element_two.second)
        return (element_one.first < element_two.first);
    return (element_one.second < element_two.second);
}

class heap {
private:
    vector<value_index> heap_list;
    int size_heap = 0;

    void heap_up(int index) {
        if (index == 0)
            return;
        int parent = (index - 1) / 2;
        if (heap_list[parent] > heap_list[index]) {
            swap(heap_list[parent], heap_list[index]);
            heap_up(parent);
        }
    }

    void heap_down(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int sup_element = index;

        if (left < size_heap && heap_list[left] < heap_list[sup_element])
            sup_element = left;
        if (right < size_heap && heap_list[right] < heap_list[sup_element])
            sup_element = right;
        if (heap_list[sup_element] < heap_list[index]) {
            swap(heap_list[index], heap_list[sup_element]);
            heap_down(sup_element);
        }
    }

public:
    void add_to_heap(value_index elements) {
        heap_list.push_back(elements);
        size_heap++;
        heap_up(size_heap - 1);
    }

    int pop() {
        int minimum = heap_list[0].first;
        swap(heap_list[0], heap_list[size_heap - 1]);
        size_heap--;
        heap_list.pop_back();
        heap_down(0);
        return minimum;
    }

    vector<int> print() {
        vector<int> new_pairs;
        for (auto i = heap_list.begin(); i != heap_list.end(); i++)
            new_pairs.push_back(i->first);
        return new_pairs;
    }

    vector<value_index> out() {
        return heap_list;
    }

};

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n, m;
    fin >> n >> m;

    heap heap_line;

    int value;
    for (int index = 0; index < n; index++) {
        fin >> value;
        heap_line.add_to_heap(make_pair(value, index));
    }

    for (int i = 0; i < m; i++) {
        int first_min = heap_line.pop();
        int second_min = heap_line.pop();
        heap_line.add_to_heap(make_pair(first_min + second_min, n));
    }

    vector<value_index> finally = heap_line.out();
    sort(finally.begin(), finally.end(), comp);
    for (auto i = finally.begin(); i != finally.end(); i++)
        fout << i->first << " ";
}
