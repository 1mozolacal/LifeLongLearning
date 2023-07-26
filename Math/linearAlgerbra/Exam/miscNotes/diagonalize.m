In linear algebra, a square matrix 
�
A is called diagonalizable or non-defective if it is similar to a diagonal matrix, i.e., if there exists an invertible matrix 
�
P and a diagonal matrix 
�
D such that 
�
−
1
�
�
=
�
{\displaystyle P^{-1}AP=D}, or equivalently 
�
=
�
�
�
−
1
{\displaystyle A=PDP^{-1}}. (Such 
�
P, 
�
D are not unique.) For a finite-dimensional vector space 
�
V, a linear map 
�
:
�
→
�
{\displaystyle T:V\to V} is called diagonalizable if there exists an ordered basis of 
�
V consisting of eigenvectors of 
�
T. These definitions are equivalent: if 
�
T has a matrix representation 
�
=
�
�
�
−
1
{\displaystyle T=PDP^{-1}} as above, then the column vectors of 
�
P form a basis consisting of eigenvectors of 
�
T, and the diagonal entries of 
�
D are the corresponding eigenvalues of 
�
T; with respect to this eigenvector basis, 
�
A is represented by 
�
D. Diagonalization is the process of finding the above 
�
P and 
�
D.

Diagonalizable matrices and maps are especially easy for computations, once their eigenvalues and eigenvectors are known. One can raise a diagonal matrix 
�
D to a power by simply raising the diagonal entries to that power, and the determinant of a diagonal matrix is simply the product of all diagonal entries; such computations generalize easily to 
�
=
�
�
�
−
1
{\displaystyle A=PDP^{-1}}. Geometrically, a diagonalizable matrix is an inhomogeneous dilation (or anisotropic scaling) — it scales the space, as does a homogeneous dilation, but by a different factor along each eigenvector axis, the factor given by the corresponding eigenvalue.

A square matrix that is not diagonalizable is called defective. It can happen that a matrix 
�
A with real entries is defective over the real numbers, meaning that 
�
=
�
�
�
−
1
{\displaystyle A=PDP^{-1}} is impossible for any invertible 
�
P and diagonal 
�
D with real entries, but it is possible with complex entries, so that 
�
A is diagonalizable over the complex numbers. For example, this is the case for a generic rotation matrix.

Many results for diagonalizable matrices hold only over an algebraically closed field (such as the complex numbers). In this case, diagonalizable matrices are dense in the space of all matrices, which means any defective matrix can be deformed into a diagonalizable matrix by a small perturbation; and the Jordan normal form theorem states that any matrix is uniquely the sum of a diagonalizable matrix and a nilpotent matrix. Over an algebraically closed field, diagonalizable matrices are equivalent to semi-simple matrices.