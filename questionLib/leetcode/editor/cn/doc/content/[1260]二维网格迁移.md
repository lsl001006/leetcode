<p>给你一个 <code>m</code> 行 <code>n</code>&nbsp;列的二维网格&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>k</code>。你需要将&nbsp;<code>grid</code>&nbsp;迁移&nbsp;<code>k</code>&nbsp;次。</p>

<p>每次「迁移」操作将会引发下述活动：</p>

<ul> 
 <li>位于 <code>grid[i][j]</code>&nbsp;的元素将会移动到&nbsp;<code>grid[i][j + 1]</code>。</li> 
 <li>位于&nbsp;<code>grid[i][n&nbsp;- 1]</code> 的元素将会移动到&nbsp;<code>grid[i + 1][0]</code>。</li> 
 <li>位于 <code>grid[m&nbsp;- 1][n - 1]</code>&nbsp;的元素将会移动到&nbsp;<code>grid[0][0]</code>。</li> 
</ul>

<p>请你返回&nbsp;<code>k</code> 次迁移操作后最终得到的 <strong>二维网格</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e1-1.png" style="height: 158px; width: 400px;" /></p>

<pre>
<span><code><strong>输入：</strong>grid</code></span> = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>输出：</strong>[[9,1,2],[3,4,5],[6,7,8]]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e2-1.png" style="height: 166px; width: 400px;" /></p>

<pre>
<span><code><strong>输入：</strong>grid</code></span> = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
<strong>输出：</strong>[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<span><code><strong>输入：</strong>grid</code></span> = [[1,2,3],[4,5,6],[7,8,9]], k = 9
<strong>输出：</strong>[[1,2,3],[4,5,6],[7,8,9]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>m ==&nbsp;grid.length</code></li> 
 <li><code>n ==&nbsp;grid[i].length</code></li> 
 <li><code>1 &lt;= m &lt;= 50</code></li> 
 <li><code>1 &lt;= n &lt;= 50</code></li> 
 <li><code>-1000 &lt;= grid[i][j] &lt;= 1000</code></li> 
 <li><code>0 &lt;= k &lt;= 100</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>矩阵</li><li>模拟</li></div></div><br><div><li>👍 90</li><li>👎 0</li></div>