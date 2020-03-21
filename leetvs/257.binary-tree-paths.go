/*
 * @lc app=leetcode id=257 lang=golang
 *
 * [257] Binary Tree Paths
 */
package main

import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
	if root == nil {
		return nil
	}
	return traversal(root, "")
}

func traversal(node *TreeNode, prefix string) []string {
	ret := make([]string, 0, 2)
	newPri := ""
	if prefix == "" {
		newPri = strconv.Itoa(node.Val)
	} else {
		newPri = prefix + "->" + strconv.Itoa(node.Val)
	}
	if node.Left == nil && node.Right == nil {
		return append(ret, newPri)
	}
	if node.Left != nil {
		ret = append(ret, traversal(node.Left, newPri)...)
	}

	if node.Right != nil {
		ret = append(ret, traversal(node.Right, newPri)...)
	}
	return ret
}

// @lc code=end

func main() {
	root := &TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}
	root.Left = &TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}
	root.Right = &TreeNode{
		Val:   3,
		Left:  nil,
		Right: nil,
	}
	root.Left.Right = &TreeNode{
		Val:   5,
		Left:  nil,
		Right: nil,
	}
	ret := binaryTreePaths(root)
	for _, v := range ret {
		println(v)
	}
}
