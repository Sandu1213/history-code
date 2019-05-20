curpath=$(cd `dirname $0`; pwd)
java -Dwebdriver.chrome.driver="$(curpath)/chromedriver" -jar server/selenium-server-standalone-3.9.0.jar