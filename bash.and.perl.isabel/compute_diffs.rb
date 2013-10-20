# requires xmllint and diff to be in the PATH

class Test

	BPELVAL_DIR = "c:/projects/bpelval-proj/tool/Testcases"
	BETSY_DIR = "c:/projects/betsy/src/main/tests/language-features"

	def self.compute_wsdl_diffs
		main_wsdl = "#{BETSY_DIR}/TestInterface.wsdl"
		partner_wsdl = "#{BETSY_DIR}/TestPartner.wsdl"

		Dir.glob("#{BPELVAL_DIR}/**/*.wsdl").each do |file|
			name = File.read(file).scan(/name="([^"\\.]*)"/)[0][0]
			if name == "TestInterface"
				wsdl = main_wsdl
			elsif name == "TestPartner"
				wsdl = partner_wsdl
			else
				raise "should not happen"
			end
			puts "Comparing #{wsdl} with #{file}"
			dirname = File.basename(File.dirname(file))
			filename = File.basename(file)
			`xmllint --c14n #{wsdl} > origin.xml`
			`xmllint --c14n #{file} > current.xml`
			`diff --ignore-space-change -U9999999 --ignore-blank-lines origin.xml current.xml > diffs/#{dirname}_WSDL_#{filename}.diff`
		end
	end

	def self.compute_bpel_diffs
		Dir.glob("#{BPELVAL_DIR}/**/*.bpel").each do |file|
			name = File.read(file).scan(/name="([^"\\.]*)"/)[0][0]
			origin = Dir.glob("#{BETSY_DIR}/**/#{name}.bpel")[0]
			dirname = File.basename(File.dirname(file))
			filename = File.basename(file)

			puts "Comparing #{origin} with #{file}"
			`xmllint --c14n #{origin} > origin.xml`
			`xmllint --c14n #{file} > current.xml`
			`diff --ignore-space-change -U9999999 --ignore-blank-lines origin.xml current.xml > diffs/#{dirname}_BPEL_#{filename}.diff`
		end
	end
end

Dir.mkdir "diffs" unless Dir.exists? "diffs"
Test.compute_wsdl_diffs
puts "------"
Test.compute_bpel_diffs