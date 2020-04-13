#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct Node {
    int key;
    struct Node *link;
} Node;

Node *head, *tail;

Node* xor(Node *a, Node *b) {
    return (Node*)((uintptr_t)a ^ (uintptr_t)b);
}

// Insertion at end
void add(int key) {
    Node *ptr = (Node*)malloc(sizeof(Node));
    ptr->key = key;

    if (head == NULL) {
        ptr->link = NULL;
        head = ptr;
        tail = ptr;
    } else {
        ptr->link = xor(tail, NULL);
        tail->link = xor(ptr, xor(tail->link, NULL));
        tail = ptr;
    }
}

void display() {
    Node *prev = NULL;
    Node *curr = head;
    Node *next;

    printf("\nList Elements: ");
    while (curr != NULL) {
        printf("%d, ", curr->key);
        next = xor(curr->link, prev);
        prev = curr;
        curr = next;
    }
}

// Returns the node at index
Node* get(int index) {
    Node *prev = NULL;
    Node *curr = head;
    Node *next;
    while (index > 0 && curr != NULL) {
        next = xor(curr->link, prev);
        prev = curr;
        curr = next;
        index--;
    }

    return curr;
}

int main() {
    int key;
    for (int i = 1; i <= 10; i++) {
        add(i);
        printf("Successfully Inserted %d\n", i);
    }

    display();

    for (int i = 9; i >= 0; i--) {
        printf("\nIndex(%d) = %d", i, get(i)->key);
    }
}