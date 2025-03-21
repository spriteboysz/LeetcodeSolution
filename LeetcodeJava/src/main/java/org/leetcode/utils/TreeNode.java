package org.leetcode.utils;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Author: Deean
 * Date: 2025-03-09 13:09
 * FileName: src/main/java/org/leetcode/utils
 * Description:
 */

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode next;
    public List<TreeNode> children;

    public TreeNode() {
    }

    public TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public TreeNode(int val, List<TreeNode> children) {
        this.val = val;
        this.children = children;
    }

    public TreeNode(int val, TreeNode left, TreeNode right, TreeNode next) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.next = next;
    }

    public TreeNode(String data) {
        if (data == null || data.isEmpty()) {
            return;
        }
        String[] dataList = data.substring(1, data.length() - 1).split(",");
        TreeNode root = new TreeNode(Integer.parseInt(dataList[0].trim()));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (i < dataList.length && !"null".equals(dataList[i].trim())) {
                node.left = new TreeNode(Integer.parseInt(dataList[i].trim()));
                queue.offer(node.left);
            }
            i++;
            if (i < dataList.length && !"null".equals(dataList[i].trim())) {
                node.right = new TreeNode(Integer.parseInt(dataList[i].trim()));
                queue.offer(node.right);
            }
            i++;
        }
        this.val = root.val;
        this.left = root.left;
        this.right = root.right;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(this);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null && !String.valueOf(node.val).equals("null")) {
                sb.append(node.val);
                queue.offer(node.left);
                queue.offer(node.right);
            } else {
                sb.append("null");
            }
            sb.append(",");
        }
        sb.append("]");
        String str = sb.toString();
        while (str.contains("null,]")) {
            str = str.replace("null,]", "]");
        }
        return str.replace(",]", "]");
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode("[1,null,3,4,5,6]");
        System.out.println(root);
    }
}
