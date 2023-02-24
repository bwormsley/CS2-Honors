package com.cinco.payroll;

abstract public class HourlyEmployee extends Employee{
	protected double hourlyPayRate;
	protected double hoursWorked;
	
	public HourlyEmployee(String id, String lastName, String firstName, String title, double hourlyPayRate,
			double hoursWorked) {
		super(id, lastName, firstName, title);
		this.hourlyPayRate = hourlyPayRate;
		this.hoursWorked = hoursWorked;
	}

	public double getHourlyPayRate() {
		return hourlyPayRate;
	}

	public double getHoursWorked() {
		return hoursWorked;
	}
	
	@Override
	public double getGrossPay() {
		return hoursWorked * hourlyPayRate;
	}
	
	
	
	
}