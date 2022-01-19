FROM ruby:3

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

WORKDIR /FL2F-master

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

CMD ["./app.rb"]