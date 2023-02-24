package com.cinco.payroll;

abstract public class Employee implements Payable {
	
	private String id;
	private String lastName;
	private String firstName;
	private String title;
	
	public Employee(String id, String lastName, String firstName, String title) {
		super();
		this.id = id;
		this.lastName = lastName;
		this.firstName = firstName;
		this.title = title;
		
		
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getName() {
		return (getLastName() + "," + getFirstName());
	}
	
	

	/**
	 * Returns a string representation (for printing) of the employee.
	 * For example, for a {@link SalaryEmployee} this method should return 
	 * <code>"Salary"</code>.
	 * 
	 * This method has been commented out to ensure the initial project
	 * compiles.  Uncomment it once you make this class abstract.
	 * 
	 * @return
	 */
	public abstract String getType();
	
	public abstract double getGrossPay();
	
	public abstract double getTaxes();
	
	public double getNetPay() {
		return getGrossPay() - getTaxes();
	}
}
	
	