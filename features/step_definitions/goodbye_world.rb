require 'rspec'

Given("there is a tired world") do
  @world = "World"
end

When("it is time to say goodbye") do
  @goodbye_world = "Goodbye " + @world
end

Then("I should say goodbye, {string}") do |string|
  expect(@goodbye_world).to eq(string)
end
