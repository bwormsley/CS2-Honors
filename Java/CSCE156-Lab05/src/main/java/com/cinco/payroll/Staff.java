package com.cinco.payroll;

public class Staff extends HourlyEmployee {

	public Staff(String id, String lastName, String firstName, String title, double hourlyPayRate, double hoursWorked) {
		super(id, lastName, firstName, title, hourlyPayRate, hoursWorked);
	}

	@Override
	public String getType() {
		return "Staff";
	}

	@Override
	public double getTaxes() {
		return getGrossPay() * 0.15;
	}
}