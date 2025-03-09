package org.leetcode.utils;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TreeNodeTest {

    @Test
    void test_001(){
        TreeNode root = new TreeNode("[1,null,3,4,5,6]");
        System.out.println(root);
        assertEquals("[1,null,3,4,5,6]", root.toString());
    }
}