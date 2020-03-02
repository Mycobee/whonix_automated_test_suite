# frozen_string_literal: true

require 'spec_helper'

context 'a running Whonix system' do
  describe 'network connectivity' do
    before do
      @conn = Faraday::Connection.new 'https://duckduckgo.com'
    end

    it 'makes a successful get request' do
      response = @conn.get
      expect(response.status).to eq(200)
    end
  end
end
