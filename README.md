# apigee-proxies

This repo contains a sample proxy that was created on apigee and exported.  Changes can be made here and imported (ie. deployed) to apigee.  For more information please refer to https://github.com/apigee/apigee-deploy-maven-plugin (but beware that some of the info seeems to be out of date and need to be found elsewhere).

Make note of the directory structure of this project.  The proxies themselves are under /gateway/*

Since there is only one set of files for a proxy, use config.json to configure the proxy based on your environments.  For example the target url may be different between test and prod so https://github.com/yemhuynh/apigee-proxies/blob/master/src/gateway/categories/config.json can be used to replace values in the proxy config before deployment.

