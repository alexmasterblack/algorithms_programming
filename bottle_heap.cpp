#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

class heap {
    vector<long long> heap_list;
    int size_heap = 0;

    void heap_up(int index) {
        if (index == 0)
            return;
        int parent = (index - 1) / 2;
        if (heap_list[parent] < heap_list[index]) {
            swap(heap_list[parent], heap_list[index]);
            heap_up(parent);
        }
    }

    void heap_down(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int sup_element = index;

        if (left < size_heap && heap_list[left] > heap_list[sup_element])
            sup_element = left;
        if (right < size_heap && heap_list[right] > heap_list[sup_element])
            sup_element = right;
        if (heap_list[sup_element] > heap_list[index]) {
            swap(heap_list[index], heap_list[sup_element]);
            heap_down(sup_element);
        }
    }

public:
    void add_to_heap(int element) {
        heap_list.push_back(element);
        size_heap++;
        heap_up(size_heap - 1);
    }

    int pop_max() {
        long long max_heap = heap_list[0];
        swap(heap_list[0], heap_list[size_heap - 1]);
        size_heap--;
        heap_list.pop_back();
        heap_down(0);
        return max_heap;
    }

    long long count_guil() {
        long long sum = 0;
        for (int i = 0; i < size_heap; i++)
            sum += heap_list[i];
        return sum;
    }
};

int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n, m;
    fin >> n >> m;

    heap thirst;

    long long sup_elem;
    for (int i = 0; i < n; i++) {
        fin >> sup_elem;
        thirst.add_to_heap(sup_elem);
    }

    for (int i = 0; i < m; i++) {
        thirst.add_to_heap(floor(thirst.pop_max() / 10));
    }

    fout << thirst.count_guil();
}