/*
 * @lc app=leetcode id=653 lang=golang
 *
 * [653] Two Sum IV - Input is a BST
 */
package main

import "log"

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

func findTarget(root *TreeNode, k int) bool {
	targets := make(map[int]int)

	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		if _, ok := targets[node.Val]; ok {
			return true
		} else {
			targets[k-node.Val] = 1
		}

		queue = queue[1:]
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return false
}

func traversal(node *TreeNode, k int, targets map[int]int) bool {
	if _, ok := targets[node.Val]; ok {
		return true
	} else {
		targets[k-node.Val] = 1
	}

	left, right := false, false
	if node.Left != nil {
		left = traversal(node.Left, k, targets)
	}
	if node.Right != nil {
		right = traversal(node.Right, k, targets)
	}
	return left || right
}

// @lc code=end

func main() {
	root := &TreeNode{
		Val:   5,
		Left:  nil,
		Right: nil,
	}
	root.Left = &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val:   2,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   4,
			Left:  nil,
			Right: nil,
		},
	}
	root.Right = &TreeNode{
		Val:  6,
		Left: nil,
		Right: &TreeNode{
			Val:   7,
			Left:  nil,
			Right: nil,
		},
	}
	log.Println(findTarget(root, 9))
	log.Println(findTarget(root, 28))
}
