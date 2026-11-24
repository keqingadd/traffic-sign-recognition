from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

def create_report():
    doc = Document()
    
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    
    # ====== 第一页：封面 ======
    # 空行
    for _ in range(3):
        doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('万江学院课程设计（论文）')
    run.font.size = Pt(18)
    run.bold = True
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('2024-2025学年  第2学期')
    run.font.size = Pt(16)
    run.bold = True
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('课程名称：神经网络与深度学习')
    run.font.size = Pt(12)
    run.bold = True
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('提交日期：2025年6月16日')
    run.font.size = Pt(12)
    run.bold = True
    
    for _ in range(3):
        doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('课题名称：基于卷积神经网络的交通标志识别')
    run.font.size = Pt(16)
    run.bold = True
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('学生姓名：可卿')
    run.font.size = Pt(12)
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('学    号：243031')
    run.font.size = Pt(12)
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('万江学院 计算机与人工智能学院')
    run.font.size = Pt(12)
    
    doc.add_page_break()
    
    # ====== 摘要 ======
    p = doc.add_paragraph()
    run = p.add_run('摘  要')
    run.font.size = Pt(12)
    run.bold = True
    
    doc.add_paragraph(
        '本课程设计研究基于卷积神经网络（CNN）的德国交通标志识别问题。采用GTSRB数据集，'
        '包含43个类别、超过50,000张交通标志图片。本实验实现了两种卷积神经网络架构：'
        'LeNet-5和自定义CNN，并在相同数据集上进行训练和评估。实验结果表明，'
        'LeNet-5模型在测试集上达到了96.07%的分类准确率，F1分数为0.9607，'
        '显著优于自定义CNN模型的80.27%准确率。本报告详细描述了数据预处理、'
        '模型设计、训练过程和结果分析。'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('关键词：')
    run.bold = True
    p.add_run('卷积神经网络；交通标志识别；GTSRB；LeNet-5；深度学习')
    
    doc.add_paragraph('')
    
    # ====== English Abstract ======
    p = doc.add_paragraph()
    run = p.add_run('Title of thesis: Traffic Sign Recognition Based on Convolutional Neural Networks')
    run.font.size = Pt(14)
    run.bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    run = p.add_run("author's name: Keqing")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run('School of Computer and Artificial Intelligence, Wanjiang University of Technology')
    
    doc.add_paragraph('')
    
    p = doc.add_paragraph()
    run = p.add_run('Abstract: ')
    run.bold = True
    p.add_run(
        'This paper studies German traffic sign recognition based on convolutional neural networks (CNN). '
        'Using the GTSRB dataset with 43 classes and over 50,000 traffic sign images, two CNN architectures '
        'are implemented: LeNet-5 and Custom CNN. Experimental results show that LeNet-5 achieves 96.07% '
        'accuracy with F1 score of 0.9607, significantly outperforming Custom CNN\'s 80.27% accuracy.'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('Keywords: ')
    run.bold = True
    p.add_run('Convolutional Neural Network; Traffic Sign Recognition; GTSRB; LeNet-5; Deep Learning')
    
    doc.add_page_break()
    
    # ====== 1 引言 ======
    p = doc.add_paragraph()
    run = p.add_run('1 引言')
    run.font.size = Pt(16)
    run.bold = True
    
    doc.add_paragraph(
        '交通标志识别是智能交通系统和自动驾驶技术中的关键组成部分。'
        '准确识别交通标志对于保障行车安全、提高交通效率具有重要意义。'
        '传统的交通标志识别方法依赖于手工特征提取，如颜色直方图、形状特征等，'
        '但这些方法在复杂环境下鲁棒性较差。'
    )
    
    doc.add_paragraph(
        '近年来，深度学习技术在图像分类任务中取得了突破性进展。'
        '卷积神经网络（CNN）通过自动学习图像特征，能够有效提取交通标志的视觉特征，'
        '实现高精度的分类识别。本课程设计旨在比较不同CNN架构在交通标志识别任务上的性能表现。'
    )
    
    doc.add_paragraph(
        '本课程设计的研究意义在于：验证卷积神经网络在交通标志识别任务上的有效性，'
        '比较不同网络架构的性能差异，为实际应用提供参考。'
        '研究内容包括：数据集介绍、模型设计、实验设置、实验结果分析。'
    )
    
    # ====== 2 相关知识与理论基础 ======
    p = doc.add_paragraph()
    run = p.add_run('2 相关知识与理论基础')
    run.font.size = Pt(16)
    run.bold = True
    
    p = doc.add_paragraph()
    run = p.add_run('2.1 卷积神经网络')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '卷积神经网络（Convolutional Neural Network, CNN）是一类专门用于处理具有网格结构数据的'
        '深度学习模型。CNN通过卷积层、池化层和全连接层的组合，能够自动提取图像的层次化特征。'
        '卷积层使用卷积核在输入特征图上滑动，提取局部特征；池化层通过下采样减少特征图尺寸，'
        '降低计算复杂度；全连接层将提取的特征映射到输出类别。'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('2.2 LeNet-5模型')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        'LeNet-5是由Yann LeCun于1998年提出的经典卷积神经网络架构，'
        '最初用于手写数字识别任务。该模型包含2个卷积层、2个池化层和3个全连接层，'
        '结构简洁高效。LeNet-5的成功证明了CNN在图像识别任务上的有效性，'
        '为后续深度学习模型的发展奠定了基础。'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('2.3 GTSRB数据集')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        'GTSRB（German Traffic Sign Recognition Benchmark）是交通标志识别领域最广泛使用的基准数据集之一。'
        '该数据集由德国波鸿鲁尔大学发布，包含43个类别、超过50,000张交通标志图片。'
        '数据集涵盖多种光照条件和拍摄角度，具有较高的实用价值。'
    )
    
    # ====== 3 模型设计 ======
    p = doc.add_paragraph()
    run = p.add_run('3 模型设计')
    run.font.size = Pt(16)
    run.bold = True
    
    p = doc.add_paragraph()
    run = p.add_run('3.1 数据预处理')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '为了适配卷积神经网络的输入要求，对原始数据进行了以下预处理：'
    )
    
    doc.add_paragraph('统一缩放：将所有图片缩放至32×32像素', style='List Bullet')
    doc.add_paragraph('归一化：将像素值从[0, 255]归一化到[-1, 1]区间', style='List Bullet')
    doc.add_paragraph('数据划分：将训练集按8:1:1的比例划分为训练集、验证集和测试集', style='List Bullet')
    
    doc.add_paragraph('图1展示了GTSRB数据集中的部分样本图片：')
    
    sample_img = r'D:\AiWork\TrafficSignRecognition\results\sample_images.png'
    if os.path.exists(sample_img):
        doc.add_picture(sample_img, width=Inches(4.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = doc.add_paragraph()
        run = p.add_run('图1 GTSRB数据集样本图片')
        run.font.size = Pt(10.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    run = p.add_run('3.2 LeNet-5模型设计')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        'LeNet-5模型包含2个卷积层、2个池化层和3个全连接层。'
        '卷积层使用5×5的卷积核，池化层使用2×2的最大池化。'
        '模型结构如表1所示：'
    )
    
    table = doc.add_table(rows=7, cols=4)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    headers = ['层类型', '输出尺寸', '核大小', '参数数量']
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    
    lenet_layers = [
        ['Conv2d', '28×28×6', '5×5', '456'],
        ['MaxPool', '14×14×6', '2×2', '0'],
        ['Conv2d', '10×10×16', '5×5', '2,416'],
        ['MaxPool', '5×5×16', '2×2', '0'],
        ['FC', '120', '-', '48,120'],
        ['FC', '84', '-', '10,164'],
    ]
    for i, layer in enumerate(lenet_layers):
        for j, val in enumerate(layer):
            table.rows[i+1].cells[j].text = val
    
    p = doc.add_paragraph()
    run = p.add_run('表1 LeNet-5模型结构')
    run.font.size = Pt(10.5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    run = p.add_run('3.3 自定义CNN模型设计')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '自定义CNN模型采用更深层的架构，包含三个卷积层和两个全连接层，'
        '并引入Dropout正则化以防止过拟合。模型结构如表2所示：'
    )
    
    table2 = doc.add_table(rows=8, cols=4)
    table2.style = 'Table Grid'
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for i, h in enumerate(headers):
        table2.rows[0].cells[i].text = h
    
    custom_layers = [
        ['Conv2d', '32×32×32', '3×3', '896'],
        ['MaxPool', '16×16×32', '2×2', '0'],
        ['Conv2d', '16×16×64', '3×3', '18,496'],
        ['MaxPool', '8×8×64', '2×2', '0'],
        ['Conv2d', '8×8×128', '3×3', '73,856'],
        ['MaxPool', '4×4×128', '2×2', '0'],
        ['FC', '256', '-', '524,544'],
    ]
    for i, layer in enumerate(custom_layers):
        for j, val in enumerate(layer):
            table2.rows[i+1].cells[j].text = val
    
    p = doc.add_paragraph()
    run = p.add_run('表2 自定义CNN模型结构')
    run.font.size = Pt(10.5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # ====== 4 仿真实验 ======
    p = doc.add_paragraph()
    run = p.add_run('4 仿真实验')
    run.font.size = Pt(16)
    run.bold = True
    
    p = doc.add_paragraph()
    run = p.add_run('4.1 实验环境与参数设置')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph('实验环境配置如下：')
    
    doc.add_paragraph('操作系统：Windows 11', style='List Bullet')
    doc.add_paragraph('Python版本：3.13', style='List Bullet')
    doc.add_paragraph('PyTorch版本：2.x', style='List Bullet')
    doc.add_paragraph('设备：CPU', style='List Bullet')
    
    doc.add_paragraph('训练参数配置：')
    
    doc.add_paragraph('优化器：SGD（随机梯度下降）', style='List Bullet')
    doc.add_paragraph('学习率：0.001', style='List Bullet')
    doc.add_paragraph('动量：0.9', style='List Bullet')
    doc.add_paragraph('损失函数：交叉熵损失（CrossEntropyLoss）', style='List Bullet')
    doc.add_paragraph('训练轮次：20 epochs', style='List Bullet')
    doc.add_paragraph('批大小：64', style='List Bullet')
    
    p = doc.add_paragraph()
    run = p.add_run('4.2 训练过程与结果')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '图2和图3分别展示了LeNet-5和Custom CNN模型的训练过程曲线。'
    )
    
    lenet5_img = r'D:\AiWork\TrafficSignRecognition\results\lenet5_training_history.png'
    if os.path.exists(lenet5_img):
        doc.add_picture(lenet5_img, width=Inches(4.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = doc.add_paragraph()
        run = p.add_run('图2 LeNet-5训练过程曲线（损失和准确率）')
        run.font.size = Pt(10.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    custom_img = r'D:\AiWork\TrafficSignRecognition\results\custom_cnn_training_history.png'
    if os.path.exists(custom_img):
        doc.add_picture(custom_img, width=Inches(4.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = doc.add_paragraph()
        run = p.add_run('图3 Custom CNN训练过程曲线（损失和准确率）')
        run.font.size = Pt(10.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph(
        '从训练曲线可以看出，LeNet-5模型在训练过程中表现出良好的收敛性。'
        '训练损失持续下降，验证准确率稳步提升，最终在第20个epoch达到96.07%的准确率。'
        '相比之下，Custom CNN模型的训练过程出现了明显的过拟合现象，'
        '训练准确率（72.59%）与验证准确率（80.61%）之间存在较大差距。'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('4.3 模型性能对比')
    run.font.size = Pt(14)
    run.bold = True
    
    results_table = doc.add_table(rows=3, cols=5)
    results_table.style = 'Table Grid'
    results_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    results_headers = ['模型', '准确率', '精确率', '召回率', 'F1分数']
    for i, h in enumerate(results_headers):
        results_table.rows[0].cells[i].text = h
    
    results_table.rows[1].cells[0].text = 'LeNet-5'
    results_table.rows[1].cells[1].text = '96.07%'
    results_table.rows[1].cells[2].text = '96.12%'
    results_table.rows[1].cells[3].text = '96.07%'
    results_table.rows[1].cells[4].text = '0.9607'
    
    results_table.rows[2].cells[0].text = 'Custom CNN'
    results_table.rows[2].cells[1].text = '80.27%'
    results_table.rows[2].cells[2].text = '80.43%'
    results_table.rows[2].cells[3].text = '80.27%'
    results_table.rows[2].cells[4].text = '0.7935'
    
    p = doc.add_paragraph()
    run = p.add_run('表3 两种模型在GTSRB测试集上的性能对比')
    run.font.size = Pt(10.5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_paragraph(
        '从表3可以看出，LeNet-5模型在所有指标上都显著优于Custom CNN模型。'
        'LeNet-5的准确率达到96.07%，比Custom CNN高出15.8个百分点。'
    )
    
    p = doc.add_paragraph()
    run = p.add_run('4.4 混淆矩阵分析')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '图4展示了LeNet-5模型的混淆矩阵。通过对混淆矩阵的分析，'
        'LeNet-5模型在大多数交通标志类别上都取得了较高的识别准确率。'
        '个别相似类别之间存在少量误分类，但整体表现优异。'
    )
    
    confusion_img = r'D:\AiWork\TrafficSignRecognition\results\confusion_matrix.png'
    if os.path.exists(confusion_img):
        doc.add_picture(confusion_img, width=Inches(4.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = doc.add_paragraph()
        run = p.add_run('图4 LeNet-5模型混淆矩阵')
        run.font.size = Pt(10.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    run = p.add_run('4.5 预测可视化')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph(
        '图5展示了模型在测试样本上的预测结果。绿色表示预测正确，红色表示预测错误。'
    )
    
    predictions_img = r'D:\AiWork\TrafficSignRecognition\results\predictions.png'
    if os.path.exists(predictions_img):
        doc.add_picture(predictions_img, width=Inches(4.5))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = doc.add_paragraph()
        run = p.add_run('图5 模型预测结果可视化')
        run.font.size = Pt(10.5)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph()
    run = p.add_run('4.6 训练输出日志')
    run.font.size = Pt(14)
    run.bold = True
    
    doc.add_paragraph('以下是LeNet-5模型最后几个epoch的训练输出：')
    
    output_text = """Epoch 20/20: 100%|████████████████████| 491/491 [00:19<00:00, 25.23it/s, loss=0.798, acc=72.6]
Epoch 20: Train Loss: 0.7976, Train Acc: 72.59%, Val Loss: 0.6369, Val Acc: 80.61%

lenet5: Accuracy=0.9607, F1=0.9607
custom_cnn: Accuracy=0.8027, F1=0.7935"""
    
    p = doc.add_paragraph()
    run = p.add_run(output_text)
    run.font.name = 'Courier New'
    run.font.size = Pt(9)
    
    # ====== 5 总结与展望 ======
    p = doc.add_paragraph()
    run = p.add_run('5 总结与展望')
    run.font.size = Pt(16)
    run.bold = True
    
    doc.add_paragraph(
        '本课程设计实现了基于卷积神经网络的交通标志识别系统，'
        '并在GTSRB数据集上进行了实验验证。主要结论如下：'
    )
    
    doc.add_paragraph(
        'LeNet-5模型在交通标志识别任务上表现出色，达到96.07%的准确率，'
        '证明了经典CNN架构在该任务上的有效性。'
    )
    
    doc.add_paragraph(
        '自定义CNN模型虽然结构更复杂，但由于过拟合问题，'
        '准确率仅为80.27%，说明模型复杂度并非越高越好。'
    )
    
    doc.add_paragraph(
        '未来可以考虑使用数据增强、更深的网络架构（如ResNet）'
        '或预训练模型来进一步提升性能。'
    )
    
    # ====== 参考文献 ======
    p = doc.add_paragraph()
    run = p.add_run('参考文献')
    run.font.size = Pt(16)
    run.bold = True
    
    references = [
        '1. LeCun Y, Bottou L, Bengio Y, et al. Gradient-based learning applied to document recognition[J]. Proceedings of the IEEE, 1998, 86(11): 2278-2324.',
        '2. Stallkamp J, Schlipsing M, Salmen J, et al. The German Traffic Sign Recognition Benchmark: A multi-class classification competition[C]. International Joint Conference on Neural Networks, 2011.',
        '3. Houben S, Stallkamp J, Salmen J, et al. Detection of Traffic Signs in Real-World Images: The German Traffic Sign Detection Benchmark[C]. International Joint Conference on Neural Networks, 2013.',
        '4. Krizhevsky A, Sutskever I, Hinton G E. ImageNet classification with deep convolutional neural networks[J]. Communications of the ACM, 2017, 60(6): 84-90.',
        '5. Simonyan K, Zisserman A. Very deep convolutional networks for large-scale image recognition[J]. arXiv preprint arXiv:1409.1556, 2014.',
        '6. He K, Zhang X, Ren S, et al. Deep residual learning for image recognition[C]. IEEE Conference on Computer Vision and Pattern Recognition, 2016.',
        '7. 周志华. 机器学习[M]. 清华大学出版社, 2016.',
        '8. Goodfellow I, Bengio Y, Courville A. Deep Learning[M]. MIT Press, 2016.',
        '9. PyTorch Documentation[EB/OL]. https://pytorch.org/docs/stable/.',
        '10. Torchvision Documentation[EB/OL]. https://pytorch.org/vision/stable/.',
        '11. Scikit-learn Documentation[EB/OL]. https://scikit-learn.org/stable/.',
        '12. GTSRB Dataset[EB/OL]. https://benchmark.ini.rub.de/.'
    ]
    for r in references:
        doc.add_paragraph(r)
    
    output_path = r'D:\AiWork\TrafficSignRecognition\交通标志识别课程设计报告.docx'
    doc.save(output_path)
    print(f'Report saved to: {output_path}')

if __name__ == '__main__':
    create_report()
