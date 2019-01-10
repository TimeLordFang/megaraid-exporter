megaraid-exporter
---

提供两种megaraid的监控方式
 - job
 - daemonset

很多可以定制化的参数暂时写死了

### job

- 至job目录下build好镜像
- 发布至k8s的物理主机上
- 用node-exporter的text collector收集对应目录下的文件

### daemonset

- 至daemonse目录下build好镜像
- 发布至k8s的物理主机上
- 集群中的prometheus会自动发现这个exporter并收集



### TODO

- nodeSelector选择只有带megasas的raid卡的物理机
- 自定义参数
- ······


#### Thanks

[repo](https://github.com/bojleros/megacli2prom)
