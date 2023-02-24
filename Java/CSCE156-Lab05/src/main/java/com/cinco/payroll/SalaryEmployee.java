package com.cinco.payroll;

public class SalaryEmployee extends Employee {
	private double annualSalary;

	public SalaryEmployee(String id, String lastName, String firstName, String title, double annualSalary) {
		super(id, lastName, firstName, title);
		this.annualSalary = annualSalary;
	}

	@Override
	public String getType() {
		return "Salary";
	}

	@Override
	public double getGrossPay() {
		return annualSalary / 52;
	}

	@Override
	public double getTaxes() {
		return getGrossPay() / 5;
	}

	@Override
	public double getNetPay() {
		return getGrossPay() - getTaxes() + 100;
	}
}