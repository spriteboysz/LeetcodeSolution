package org.leetcode.utils;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ListNodeTest {
    @Test
    void test_001() {
        ListNode node = new ListNode(0, null);
        System.out.println(node);
        ListNode head = new ListNode(new int[]{1, 2, 3});
        System.out.println(head);
        var head2 = new ListNode("[1,2,3,4,5]");
        System.out.println(head2);
        assertEquals("[1, 2, 3, 4, 5]", head2.toString());
    }
}