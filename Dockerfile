#FROM ruby:2-alpine as jekyll

#RUN apk add --no-cache build-base gcc bash cmake git

#RUN gem install bundler -v "~>1.0" && gem install bundler jekyll


#WORKDIR /FL2F-master
#COPY Gemfile Gemfile.lock ./

#FROM jekyll as jekyll-serve
    
#COPY . ./

#CMD [ "bundle", "exec", "jekyll", "serve"]
#-----------------------------------------
FROM ruby:2-alpine as jekyll

RUN apk add --no-cache build-base gcc bash cmake git

# install both bundler 1.x and 2.x incase you're running
# old gem files
# https://bundler.io/guides/bundler_2_upgrade.html#faq
RUN gem install bundler -v "~>1.0" && gem install bundler jekyll

EXPOSE 8080

WORKDIR /FL2F-master

ENTRYPOINT [ "jekyll" ]

CMD [ "--help" ]


FROM jekyll as jekyll-serve

COPY Gemfile Gemfile.lock ./
COPY . ./

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh && ln -s /usr/local/bin/docker-entrypoint.sh /
# on every container start, check if Gemfile exists and warn if it's missing
ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD [ "bundle", "exec", "jekyll", "serve", "--force_polling", "-H", "0.0.0.0", "-P", "8080" ]