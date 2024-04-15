# week 6 과제
cd ~/etc/reference
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr1.fa.gz  
bwa index chr1.fa.gz  
cd ~/Analysis.sample  
bwa mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ~/etc/regerence/chr1.fa.gz sample_1.fastq.gz sample_2.fastq.gz > sample.sam  
samtools sort sample.chr1.mapped.bam -o sample.chr1.sorted.bam  
samtools index sample.chr1sorted.bam  
samtools tview sample.chr1.sorted.bam  