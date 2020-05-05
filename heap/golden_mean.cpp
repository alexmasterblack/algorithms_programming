#include <vector>
#include <fstream>
#include <iostream>

using namespace std;

class heap_max {
    vector<long long> heap_list;
    int size_heap = 0;

    void heap_max_up(int index) {
        if (index == 0)
            return;
        int parent = (index - 1) / 2;
        if (heap_list[parent] < heap_list[index]) {
            swap(heap_list[parent], heap_list[index]);
            heap_max_up(parent);
        }
    }

    void heap_max_down(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int sup_element = index;

        if (left < size_heap && heap_list[left] > heap_list[sup_element])
            sup_element = left;
        if (right < size_heap && heap_list[right] > heap_list[sup_element])
            sup_element = right;
        if (heap_list[sup_element] > heap_list[index]) {
            swap(heap_list[index], heap_list[sup_element]);
            heap_max_down(sup_element);
        }
    }

public:

    void add_to_heap(int element) {
        heap_list.push_back(element);
        size_heap++;
        heap_max_up(size_heap - 1);
    }

    int pop() {
        long long max_heap = heap_list[0];
        swap(heap_list[0], heap_list[size_heap - 1]);
        size_heap--;
        heap_list.pop_back();
        heap_max_down(0);
        return max_heap;
    }

    int top() {
        return heap_list[0];
    }
};

class heap_min {
    vector<long long> heap_list;
    int size_heap = 0;

    void heap_min_up(int index) {
        if (index == 0)
            return;
        int parent = (index - 1) / 2;
        if (heap_list[parent] > heap_list[index]) {
            swap(heap_list[parent], heap_list[index]);
            heap_min_up(parent);
        }
    }

    void heap_min_down(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int sup_element = index;

        if (left < size_heap && heap_list[left] < heap_list[sup_element])
            sup_element = left;
        if (right < size_heap && heap_list[right] < heap_list[sup_element])
            sup_element = right;
        if (heap_list[sup_element] < heap_list[index]) {
            swap(heap_list[index], heap_list[sup_element]);
            heap_min_down(sup_element);
        }
    }

public:

    void add_to_heap(int element) {
        heap_list.push_back(element);
        size_heap++;
        heap_min_up(size_heap - 1);
    }

    int pop() {
        long long min_heap = heap_list[0];
        swap(heap_list[0], heap_list[size_heap - 1]);
        size_heap--;
        heap_list.pop_back();
        heap_min_down(0);
        return min_heap;
    }

    int top() {
        return heap_list[0];
    }
};

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n;

    heap_max left_max;
    heap_min right_min;

    int sup_element;

    vector<int> sup_arr;

    for (int index = 0; index < n; index++) {
        fin >> sup_element;
        if (index == 0)
            left_max.add_to_heap(sup_element);
        else {
            if (index % 2 != 0) {
                if (sup_element < left_max.top()) {
                    right_min.add_to_heap(left_max.pop());
                    left_max.add_to_heap(sup_element);
                } else
                    right_min.add_to_heap(sup_element);
            }
            if (index % 2 == 0) {
                if (sup_element > right_min.top()) {
                    left_max.add_to_heap(right_min.pop());
                    right_min.add_to_heap(sup_element);
                } else
                    left_max.add_to_heap(sup_element);
            }
        }
        sup_arr.push_back(left_max.top());
    }

    for (int i = 0; i < n; i++) {
        fout << sup_arr[i] << " ";
    }
}
