from qiskit import QISKitError, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

if __name__ == '__main__':

    try:

        # Prepare program
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        qc = QuantumCircuit(q, c)

        # Put qubit in superposition
        qc.x(q[0])

        # Measure quantum state
        qc.measure(q, c)

        # Execute program
        job_sim = execute(qc, "local_qasm_simulator")
        sim_result = job_sim.result()
        print("simulation: ", sim_result)
        print(sim_result.get_counts(qc))

    except QISKitError as ex:
        print('Quantum fluctuations! Eh Gad!'.format(ex))
