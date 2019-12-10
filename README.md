# apigee-proxies

This repo contains a sample proxy that was created on apigee and exported.  Changes can be made here and imported (ie. deployed) to apigee.  For more information please refer to [apigee-deploy-maven-plugin](https://github.com/apigee/apigee-deploy-maven-plugin) (but beware that some of the info seeems to be out of date and need to be found elsewhere).

Make note of the directory structure of this project.  The proxies themselves are under /gateway/*

Since there is only one set of files for a proxy, use config.json to configure the proxy based on your environments.  For example the target url may be different between test and prod so [config.json](https://github.com/yemhuynh/apigee-proxies/blob/master/src/gateway/categories/config.json) can be used to replace values in the proxy config before deployment.

Some commands to get started:

```
To configure/package the proxy to be deployed (but does not deploy):

mvn package -P<maven_profile> -Dusername=<your_apigee_username> -Dpassword=<your_apigee_password> -Dorg=<your_apigee_org>

Example:

mvn package -Pprod -Dusername=somename@somehost.com -Dpassword=foobar -Dorg=somename-eval

In the above example the profile is prod (see shared-pom.xml) to org=somename-eval (this appears in the top left hand corner of your apigee interface when you log in).  
```

```
To configure/package and deploy and update an existing version (in this example version 6) :

mvn package -P<maven_profile> -Dusername=<your_apigee_username> -Dpassword=<your_apigee_password> -Dorg=<your_apigee_org>
```

```
To configure/package and deploy to the next version (ie if the latest version is 3 then this will deploy a version 4) 

mvn install -P<maven_profile> -Dusername=<your_apigee_username> -Dpassword=<your_apigee_password> -Dorg=<your_apigee_org>
```
