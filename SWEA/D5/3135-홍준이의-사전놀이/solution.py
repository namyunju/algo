#include <iostream>
/*
insert
단어의 길이와 단어가 주어지면 공책에 추가

query
문자열 길이와 문자열 주어지면 해당 문자열로 시작하는 단어의 개수 반환
*/
/*
문자열 저장과 검색 문제.
Trie

문자열 공통 prefix를 공유해서 저장.
각 노드에 그 다음에 올 문자 노드를 넣


최대 연산 횟수 10만, 문자열 최대 길이 10
최악의 경우 백만 노드
*/
#define MAX_NODE 1000001

// 문자 하나당 노드 하나 
struct TrieNode {
    // 현재 노드 다음에 올 수 있는 문자
    // child[0]은 a, child[1]은 b ... 
    int child[26];
    
    //이 노드를 지나간 단어의 개수
    int cnt;
};

// Trie에서 사용할 모든 노드 배열. trie[0]은 root
TrieNode trie[MAX_NODE];

// 현재까지 사용한 노드 개수
int nodeCnt;

// 노드 번호를 받아 Trie의 idx 노드를 초기화
void clearNode(int idx) {
    trie[idx].cnt = 0;

    for (int i = 0; i <26; i++) {
        trie[idx].child[i] = 0;
    }
}

void init() {
    // root가 있으므로 1부터 시작
    nodeCnt = 1;
    // root 초기화
    clearNode(0);
}

// 문자열 추가
void insert(int buffer_size, char *buf) {
    int cur = 0;

    for (int i = 0; i < buffer_size; i++) {
        // i번째 문자를 숫자로 변환
        int c = buf[i] - 'a';

        // 현재 노드에 해당 자식 노드가 없다면 새 노드 생성
        if (trie[cur].child[c] == 0) {
            trie[cur].child[c] = nodeCnt;
            clearNode(nodeCnt);
            nodeCnt++;
        }
        // 해당 노드로 이동하고 다음 문자 작업 이어감
        cur = trie[cur].child[c];
        trie[cur].cnt++;
    }
}

// buf로 시작하는 문자 개수 반환
int query(int buffer_size, char *buf) {
    // root에서 시작
    int cur = 0;

    for (int i = 0; i < buffer_size; i++) {
        int c = buf[i] - 'a';
        // 타고타고 들어가다 노드가 없다면 단어가 없다는 뜻
        if (trie[cur].child[c] == 0) {
            return 0;
        }

        cur = trie[cur].child[c];
    }
    return trie[cur].cnt;
}