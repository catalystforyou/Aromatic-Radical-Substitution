# Aromatic-Radical-Substitution
这一部分工作呈现的内容是对https://doi.org/10.1002/anie.202000959 文献的部分复现，量化计算通过Gaussian进行，主要描述符的计算通过Multiwfn实现。大致流程如下：
- 绘制结构，将SMILES保存在Ar.smi中，在其后逐对添加反应位点和产率，以空格分隔；并将Chem3D或RDkit优化过的三维结构保存为Gaussian输入文件，利用gjf_Generator.py设定需要的计算方法和基组，传入服务器上的Gaussian进行结构优化
- 将得到的输出文件用log2gjf.py批量转化为优化好结构的输入文件，再利用Descriptors_input_trans_new.py得到三种不同电荷模式下的输入文件，传入服务器上的Gaussian进行NBO计算
- 将chk文件均转化为fchk文件，再利用fchk2wfn.py转化为wfn文件，调用Multiwfn从三种电荷下的wfn导出描述符
- 利用get_dscp.py将导出的描述符和Ar.smi中的反应位点与产率数据一一对应，导出为merge_table.csv，每一行对应一个反应位点上发生的反应
- 在Regressor.py中进行回归拟合

目前的反应条目一共有104条，A、C、E、G代表着四种不同的自由基，其后的数字意味着在这个自由基对应的取代反应中的编号。

之后可以进行的改进：
- 将反应产率预测变为反应位点预测，但具有多个位点反应数据的分子较少
- 将自由基的描述符也纳入数据的一部分
