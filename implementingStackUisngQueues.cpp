#include<iostream>
class MyStack {
public:
    queue<int>q1, q2;
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        if(!q1.empty()){
            while(q1.size()!= 1){
                q2.push(q1.front());
                q1.pop();
            }
            int x = q1.front();
            q1.pop();
            return x;
        }
        while(q2.size()!=1){
            q1.push(q2.front());
            q2.pop();
        }
        int x = q2.front();
        q2.pop();
        return x;
    }
    
    int top() {
        if(!q1.empty())return q1.back();
        return q2.back();
    }
    
    bool empty() {
        return q1.empty() && q2.empty();
        
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */