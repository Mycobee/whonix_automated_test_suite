require 'rspec'

Given("there is an awake world") do
  @world = "World"
end

When("it is time to say hello") do
  @hello_world = "Hello " + @world
end

Then("I should say hello, {string}") do |string|
  expect(@hello_world).to eq(string)
end
