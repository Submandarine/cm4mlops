# MLPerf Inference Benchmarking on AWS dl2q.24xlarge instance using 8 QAIC Cloud AI 100

`dl2q.24xlarge` instance is available in `us-west-2d` and it has 96 vCPUs and 768 GB of memory. 

[Deep Learning Base Qualcomm AMI (Amazon Linux 2) 20231213, ami-08cae482e3b14c9b8](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstances:ami=ami-08cae482e3b14c9b8) image from the Community AMIs is the recommended OS image as it comes with the QIAC SDKs (both Apps and Platform) preinstalled.

* Recommended to take 300 GB root disk


## System setup
```
sudo yum install -y python3-devel git
python3.8 -m pip install cmind
cm pull repo mlcommons@ck
cm run script --tags=get,python --version_min=3.8.1
```

## Bert-99

### Quick performance run
```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic \
--backend=glow --scenario=Offline  --implementation=kilt --model=bert-99 \
--test_query_count=40000 --precision=uint8 --rerun --quiet \
--adr.mlperf-inference-implementation.tags=_loadgen-batch-size.4096,_dl2q.24xlarge \
--quiet --adr.compiler.tags=gcc --execution-mode=test
```

### Full valid run
```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic \
--backend=glow --scenario=Offline --implementation=kilt --model=bert-99 --precision=uint8 \
--adr.mlperf-inference-implementation.tags=_loadgen-batch-size.4096,_dl2q.24xlarge \
--rerun --quiet --execution-mode=valid
```

The expected performance is ~5700 QPS

### Accuracy run
```
cm run script --tags=generate-run-cmds,inference,_accuracy-only --device=qaic \
--backend=glow --scenario=Offline --implementation=kilt --model=bert-99 --precision=uint8 \
--adr.mlperf-inference-implementation.tags=_loadgen-batch-size.4096,_dl2q.24xlarge \
--rerun --quiet --execution-mode=valid
```

The expected accuracy is ~90



## ResNet50

### Quick performance run

```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--test_query_count=400000 --precision=uint8 --rerun --adr.compiler.tags=gcc \
--adr.mlperf-inference-implementation.tags=_bs.8,_dl2q.24xlarge --execution-mode=test
```

### Full valid run

```
cm run script --tags=generate-run-cmds,inference,_performance-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--test_query_count=400000 --precision=uint8 --rerun --adr.compiler.tags=gcc \
--adr.mlperf-inference-implementation.tags=_bs.8,_dl2q.24xlarge --execution-mode=valid
```
Expected performance is ~157500

### Accuracy run

```
cm run script --tags=generate-run-cmds,inference,_accuracy-only --device=qaic --backend=glow \
--scenario=Offline  --implementation=kilt --model=resnet50 \
--test_query_count=400000 --precision=uint8 --rerun --adr.compiler.tags=gcc \
--adr.mlperf-inference-implementation.tags=_bs.8,_dl2q.24xlarge --execution-mode=valid
```

Expected accuracy is 75.936%


## RetinaNet

*TODO*